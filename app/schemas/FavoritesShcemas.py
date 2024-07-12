from marshmallow import Schema, fields, validate


class FavoriteSchema(Schema):
    id = fields.Int(dump_only=True)
    created = fields.Str(dump_only=True)
    modified = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    description = fields.Str(required=False)
    swapi_id = fields.Str(required=True)
    type = fields.Str(required=True)


class FavoritePostSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=6))
    description = fields.Str(required=False, validate=validate.Length(min=0))
    swapi_id = fields.Str(required=True, validate=validate.Length(min=1))
    type = fields.Str(required=True, validate=validate.OneOf(['films', 'people', 'planets', 'starships', 'vehicles', 'species']))

class FavoritePutSchema(Schema):
    description = fields.Str(required=False, validate=validate.Length(min=0))