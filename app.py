import os

from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect, flash

from extensions import db, migrate
import models
from forms import CursoForm, EliminarCursoForm
from services.curso_service import (
    agregar_curso,
    obtener_todos,
    obtener_por_id,
    editar_curso,
    eliminar_curso,
)

load_dotenv()
app = Flask(__name__)

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)
migrate.init_app(app, db)

@app.route("/")
def index():
    cursos = obtener_todos()
    eliminar_form = EliminarCursoForm()
    return render_template("index.html", cursos=cursos, eliminar_form=eliminar_form)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    form = CursoForm()

    if form.validate_on_submit():
        agregar_curso(
            nombre=form.nombre.data,
            instructor=form.instructor.data,
            duracion=form.duracion.data
        )
        flash("Curso agregado correctamente.", "success")
        return redirect(url_for("index"))
    return render_template("agregar_curso.html", form=form)

@app.route("/editar/<int:id_curso>", methods=["GET", "POST"])
def editar(id_curso):
    curso = obtener_por_id(id_curso)

    if curso is None:
        flash("El curso solicitado no existe.", "danger")
        return redirect(url_for("index"))

    form = CursoForm(obj=curso)

    if form.validate_on_submit():
        editar_curso(
            curso=curso,
            nombre=form.nombre.data,
            instructor=form.instructor.data,
            duracion=form.duracion.data
        )
        flash("Curso actualizado correctamente.", "success")
        return redirect(url_for("index"))

    return render_template("editar_curso.html", form=form, curso=curso)

@app.route("/eliminar/<int:id_curso>", methods=["POST"])
def eliminar(id_curso):
    curso = obtener_por_id(id_curso)

    if curso is None:
        flash("El curso solicitado no existe.", "danger")
        return redirect(url_for("index"))

    eliminar_form = EliminarCursoForm()

    if not eliminar_form.validate_on_submit():
        flash("La solicitud de eliminación no es válida.", "danger")
        return redirect(url_for("index"))

    eliminar_curso(curso)

    flash("Curso eliminado correctamente.", "success")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
