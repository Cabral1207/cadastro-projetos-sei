from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config['SECRET_KEY'] = 'chave-secreta'

    from .auth import bp as bp_auth
    app.register_blueprint(bp_auth)

    from .projetos import bp as bp_projetos
    app.register_blueprint(bp_projetos)

    from .usuarios import bp as bp_usuarios
    app.register_blueprint(bp_usuarios)
    return app
