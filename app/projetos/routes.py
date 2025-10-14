from flask import render_template
from . import bp

@bp.route("/projetos")
def cadastro_projeto():
    print("alguma coisa")
    return render_template("projetos.html")

@bp.route("/editar_projetos")
def editar_projeto():
    print("alguma coisa")
    return render_template("editar-projeto.html")
