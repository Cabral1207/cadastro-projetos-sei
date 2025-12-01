from flask import flash, redirect, render_template, request

from app.usuarios.models import Usuario
from . import bp

@bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        matricula = request.form["matricula"]
        senha = request.form["senha"]
        usuario_cadastrado = Usuario.procurar_por_matricula(matricula=matricula, senha=senha)
        if usuario_cadastrado == None:
            Usuario.create_user(matricula=matricula, senha=senha)
            flash("USUÁRIO CADASTRADO COM SUCESSO")
        flash("Usuário já cadastrado")
        return redirect("cadastro")
    return render_template("cadastro-2.html")

@bp.route("/detalhes_professor", methods=["GET", "POST"])
def detalhes_professor():
    return render_template("projeto-detalhes-professor.html")


@bp.route("/professor", methods=["GET", "POST"])
def home_professor():
    return render_template("tela-professor.html")
