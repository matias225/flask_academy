import os

from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect, flash

from extensions import db, migrate
import models
from forms import CursoForm
from services.curso_service import agregar_curso, obtener_todos

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

    return render_template("index.html", cursos=cursos)

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

if __name__ == "__main__":
    app.run(debug=True)
