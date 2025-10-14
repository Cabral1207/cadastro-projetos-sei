from flask import request, flash, redirect, render_template, session, url_for

from models import Usuario
from . import bp

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form["matricula"]
        senha = request.form["senha"]
        print(username)
        print(senha)
        user = Usuario.procurar_por_matricula(matricula=username, senha=senha)
        print(user)
        if not user:
            flash(f'Erro ao efetuar login, verifique os dados e tente novamente')
        if user:
            session["usuario"] = {
                "username": username,
                "senha": senha
            }
            return redirect(url_for("auth.home"))
    return render_template("login-sem-js.html")

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/logout", methods=["GET", "POST"])
def logout():
    session["usuario"] = None
    return redirect("login")