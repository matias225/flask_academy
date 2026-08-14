from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class CursoForm(FlaskForm):
    nombre = StringField("Nombre del curso", validators=[
            DataRequired(message="El nombre del curso es obligatorio."),
            Length(min=2, max=150, message="El nombre debe tener entre 2 y 150 caracteres.")
    ])
    instructor = StringField("Instructor", validators=[
            DataRequired(message="El instructor es obligatorio."),
            Length(min=2, max=150, message="El instructor debe tener entre 2 y 150 caracteres.")
    ])
    duracion = DecimalField("Duración", places=2, validators=[
            DataRequired(message="La duración es obligatoria."),
            NumberRange(min=0.01, message="La duración debe ser mayor que 0.")
    ])
    submit = SubmitField("Guardar curso")

class EliminarCursoForm(FlaskForm):
    submit = SubmitField("Eliminar")
