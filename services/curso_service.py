from models import Curso
from extensions import db

def obtener_todos():
    return Curso.query.all()

def obtener_por_id(id_curso):
    return db.session.get(Curso, id_curso)

def agregar_curso(nombre, instructor, duracion):
    curso = Curso(
        nombre=nombre,
        instructor=instructor,
        duracion=duracion
    )

    db.session.add(curso)
    db.session.commit()
    return curso

def editar_curso(curso, nombre, instructor, duracion):
    curso.nombre = nombre
    curso.instructor = instructor
    curso.duracion = duracion

    db.session.commit()
    return curso

def eliminar_curso(curso):
    db.session.delete(curso)
    db.session.commit()
