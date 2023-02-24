from marshmallow import fields

from api import ma

from ..models import curso_model


class CursoSchema(ma.SQLAlchemyAutoSchema):
    model = curso_model.Curso
    loas_instance = True
    fields = ("id", "nome", "descricao", "data-publicacao")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_publicacao = fields.Date(required=True)
