from extensions import db

class Curso(db.Model):
    __tablename__ = "curso"

    id_curso = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    nombre = db.Column(
        db.String(150),
        nullable=False
    )
    instructor = db.Column(
        db.String(150),
        nullable=False
    )
    duracion = db.Column(
        db.Numeric(5, 2),
        nullable=False
    )
