from flask import Blueprint
bp = Blueprint("usuario", __name__, template_folder="../../templates/")
from . import routes