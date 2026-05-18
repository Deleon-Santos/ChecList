
from flask import  Blueprint, request, jsonify
# from flask import blueprints

from controllers.controller import add_lemmbrete, logar, pegar_lembretes


main = Blueprint('main', __name__)

@main.route("/index")
def index():
    return "Hello, World!"

@main.route("/login", methods=["POST"])
def login():
    user = request.get_json() or {}
    if user.get("email") and user.get("senha"):
        print(user)
        return logar(user.get("email"), user.get("senha"))
    return jsonify({"error": "Dados incompletos"}), 400


@main.route("/lembrete", methods=["POST"])
def criar_lembrete():
    lembrete = request.get_json() or {}
    if lembrete.get("titulo") and lembrete.get("descricao") and lembrete.get("data_hora") and lembrete.get("user") and lembrete.get("status"):
        print(lembrete) 
        return add_lemmbrete(lembrete)
        #return jsonify({"message": "Lembrete criado com sucesso!"}), 201
    return jsonify({"error": "Dados incompletos"}), 400


@main.route("/lembrete", methods=["GET"])
def lembretes():
    return pegar_lembretes()
    