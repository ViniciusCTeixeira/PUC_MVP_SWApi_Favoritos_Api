from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from app import api, db
from app.models.FavoritesModel import Favorite
from app.schemas.FavoritesShcemas import FavoriteSchema, FavoritePostSchema, FavoritePutSchema
from app.api_models.Favorites import DefineApiFavoritesModels
from app.api_models.Erros import DefineApiErrosModels
import requests

favorites_ns = Namespace('Favoritos', description='Gerenciamento de favoritos')

api_favorite_models = DefineApiFavoritesModels(api)
api_error_models = DefineApiErrosModels(api)


def verify_swapi_id(type, swapi_id):
    response = requests.get(f"https://swapi.dev/api/{type}/{swapi_id}/")
    return response.status_code == 200


@favorites_ns.route('/')
class FavoriteList(Resource):
    @favorites_ns.response(200, 'Success', api_favorite_models['favorite_response_model'], as_list=True)
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def get(self):
        try:
            favorites = Favorite.query.all()
            return FavoriteSchema(many=True).dump(favorites), 200
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500

    @favorites_ns.expect(api_favorite_models['favorite_post_model'])
    @favorites_ns.response(201, 'Created', api_favorite_models['favorite_response_model'], as_list=False)
    @favorites_ns.response(400, 'Validation Error', api_error_models['error_model'])
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def post(self):
        try:
            data = FavoritePostSchema().load(request.json)
            if not verify_swapi_id(data['type'], data['swapi_id']):
                return {"message": "swapi_id inválido", 'errors': ''}, 400

            new_favorite = Favorite(
                username=data['username'],
                description=data['description'],
                swapi_id=data['swapi_id'],
                type=data['type']
            )

            new_favorite.save()

            return FavoriteSchema().dump(new_favorite), 201
        except ValidationError as err:
            return {"message": "Erro de validação", "errors": err.messages}, 400
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500


@favorites_ns.route('/<string:username>/')
@favorites_ns.param('username', 'Nome de usuário')
class FavoriteDetailByUsername(Resource):
    @favorites_ns.response(200, 'Success', api_favorite_models['favorite_response_model'], as_list=True)
    @favorites_ns.response(400, 'Validation Error', api_error_models['error_model'])
    @favorites_ns.response(404, 'Not Found', api_error_models['error_model'])
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def get(self, username):
        try:
            favorite = Favorite.query.filter_by(username=username).all()
            if not favorite:
                return {"message": "Favorito não encontrado"}, 404
            return FavoriteSchema(many=True).dump(favorite), 200
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500


@favorites_ns.route('/<int:id>/<string:username>/')
@favorites_ns.param('id', 'Identificador do favorito')
@favorites_ns.param('username', 'Nome de usuário')
class FavoriteDetailByIdUsername(Resource):
    @favorites_ns.response(200, 'Success', api_favorite_models['favorite_response_model'], as_list=False)
    @favorites_ns.response(400, 'Validation Error', api_error_models['error_model'])
    @favorites_ns.response(404, 'Not Found', api_error_models['error_model'])
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def get(self, id, username):
        try:
            favorite = Favorite.query.filter_by(id=id, username=username).first()
            if not favorite:
                return {"message": "Favorito não encontrado"}, 404
            return FavoriteSchema().dump(favorite), 200
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500

    @favorites_ns.expect(api_favorite_models['favorite_put_model'])
    @favorites_ns.response(200, 'Updated', api_favorite_models['favorite_response_model'], as_list=False)
    @favorites_ns.response(400, 'Validation Error', api_error_models['error_model'])
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def put(self, id, username):
        try:
            data = FavoritePutSchema().load(request.json)

            favorite = Favorite.query.filter_by(id=id, username=username).first()

            if not favorite:
                return {"message": "Favorito não encontrado"}, 404

            favorite.description = data['description']

            favorite.update()
            return FavoriteSchema().dump(favorite), 200
        except ValidationError as err:
            return {"message": "Erro de validação", "errors": err.messages}, 400
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500


    @favorites_ns.response(204, 'Deleted', api_favorite_models['favorite_delete_model'], as_list=False)
    @favorites_ns.response(400, 'Validation Error', api_error_models['error_model'])
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def delete(self, id, username):
        try:

            favorite = Favorite.query.filter_by(id=id, username=username).first()

            if not favorite:
                return {"message": "Favorito não encontrado"}, 404

            favorite.delete()
            return {"message": "Favorito removido"}, 204
        except ValidationError as err:
            return {"message": "Erro de validação", "errors": err.messages}, 400
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500


@favorites_ns.route('/<string:type>/<string:username>/')
@favorites_ns.param('type', 'Tipo do favorito')
@favorites_ns.param('username', 'Nome de usuário')
class FavoriteDetailByTypeUsername(Resource):
    @favorites_ns.response(200, 'Success', api_favorite_models['favorite_response_model'], as_list=True)
    @favorites_ns.response(404, 'Not Found', api_error_models['error_model'])
    @favorites_ns.response(500, 'Internal Server Error', api_error_models['error_model'])
    def get(self, type, username):
        try:
            favorite = Favorite.query.filter_by(type=type, username=username).all()
            if not favorite:
                return {"message": "Favorito não encontrado"}, 404
            return FavoriteSchema(many=True).dump(favorite), 200
        except Exception as e:
            return {"message": "Erro interno no servidor", "errors": str(e)}, 500


api.add_namespace(favorites_ns, path='/favorites')
