
from flask import  Blueprint, request, jsonify
# from flask import blueprints

from controllers.controller import add_lemmbrete


main = Blueprint('main', __name__)

@main.route("/index")
def index():
    return "Hello, World!"

@main.route("/lembrete", methods=["POST"])
def criar_lembrete():
    lembrete = request.get_json() or {}
    if lembrete.get("titulo") and lembrete.get("descricao") and lembrete.get("data_hora") and lembrete.get("user") and lembrete.get("status"):
        print(lembrete) 
        add_lemmbrete(lembrete)
        return jsonify({"message": "Lembrete criado com sucesso!"}), 201
    return jsonify({"error": "Dados incompletos"}), 400
