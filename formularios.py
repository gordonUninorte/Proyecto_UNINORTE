from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class formularioMensaje(FlaskForm):
    autor= StringField('Autor', validators=[DataRequired(message='Por favor escriba un autor')])
    destinatario= StringField('Para', validators=[DataRequired(message='Por favor escriba un destinatario')])
    enviar = SubmitField('Enviar')


