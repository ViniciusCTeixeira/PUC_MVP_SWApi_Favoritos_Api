from flask_restx import fields, Api

def DefineApiFavoritesModels(api: Api):
    favorite_response_model = api.model('Favorite Response', {
        'id': fields.String(required=True, description='Nome de usuário'),
        'created': fields.String(required=True, description='Data de criação'),
        'modified': fields.String(required=True, description='Data da ultima alteração'),
        'username': fields.String(required=True, description='Nome de usuário'),
        'description': fields.String(required=False, description='Descrição do favorito'),
        'swapi_id': fields.String(required=True, description='ID no SWAPI'),
        'type': fields.String(required=True, description='Tipo do favorito (films, people, planets, starships, vehicles, species)')
    })
    favorite_post_model = api.model('Favorite Post', {
        'username': fields.String(required=True, description='Nome de usuário'),
        'description': fields.String(required=False, description='Descrição do favorito'),
        'swapi_id': fields.String(required=True, description='ID no SWAPI'),
        'type': fields.String(required=True, description='Tipo do favorito (films, people, planets, starships, vehicles, species)')
    })
    favorite_put_model = api.model('Favorite Put', {
        'description': fields.String(required=False, description='Descrição do favorito'),
    })
    favorite_delete_model = api.model('Favorite Delete', {
        'message': fields.String(required=True, description='Mensagem'),
    })
    return {
        'favorite_response_model': favorite_response_model,
        'favorite_post_model': favorite_post_model,
        'favorite_put_model': favorite_put_model,
        'favorite_delete_model': favorite_delete_model,
    }