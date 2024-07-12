from flask_restx import fields, Api

def DefineApiErrosModels(api: Api):
    error_model = api.model('Error', {
        'message': fields.String(required=True, description='Mensagem de erro'),
        'errors': fields.Raw(description='Detalhes adicionais sobre o erro')
    })

    return {
        'error_model': error_model
    }