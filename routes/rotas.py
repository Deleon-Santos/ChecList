from flask import Blueprint, request, jsonify, render_template, send_from_directory
from flask_jwt_extended import get_jwt_identity,jwt_required
from controllers.controller import add_lembrete, atualizar_lembrete_id, deletar_lembrete_id, logar, novo_user, pegar_lembrete_id, pegar_lembretes
from model.models import User, Lembrete

main = Blueprint('main', __name__)

@main.route("/api")
def openapi():
    return send_from_directory("static", "openapi.json")


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/cadastro", methods=["POST"])
def cadastro():
    user = request.get_json() or {}
    if user.get("email") and user.get("senha") and user.get("nome"):
        
        return novo_user(user.get("nome"), user.get("email"), user.get("senha"))
    return jsonify({"error": "Dados incompletos"}), 400


@main.route("/login", methods=["POST"])
def login():
    user = request.get_json() or {}
    if user.get("email") and user.get("senha"):
        # print(user)
        return logar(user.get("email"), user.get("senha"))
    return jsonify({"error": "Dados incompletos"}), 400


@main.route("/lembrete", methods=["POST"])
@jwt_required()
def criar_lembrete():
    user = get_jwt_identity()
    if not user:
        return jsonify({"error": "Usuário não autenticado."}), 401
    lembrete = request.get_json() or {}
    
    if lembrete.get("titulo") and lembrete.get("descricao") and lembrete.get("user") and lembrete.get("status") and lembrete.get("area") and lembrete.get("prioridade"): 
        return add_lembrete(lembrete.get("titulo"), lembrete.get("descricao"),lembrete.get("user"),lembrete.get("status"),lembrete.get("area"),lembrete.get("prioridade"))
    return jsonify({"error": "Dados incompletos"}), 400


@main.route("/lembrete", methods=["GET"])
@jwt_required()
def lembretes():
    user = get_jwt_identity()
    if not user:
        return jsonify({"error": "Usuário não autenticado."}), 401
    return pegar_lembretes()
    

@main.route("/lembrete_id/<int:id_lembrete>", methods=["GET"])
@jwt_required()
def lembrete_id(id_lembrete):
    user = get_jwt_identity()
    if not user:
        return jsonify({"error": "Usuário não autenticado."}), 401
    if id_lembrete:
        return pegar_lembrete_id(id_lembrete)
    return jsonify({"error": "ID do lembrete é necessário"}), 400


@main.route("/deleta_id/<int:id_lembrete>", methods=["DELETE"])
@jwt_required()
def deletar_lembrete(id_lembrete):
    user = get_jwt_identity()
    status = request.get_json() or ("excluído",)
    if not user:
        return jsonify({"error": "Usuário não autenticado."}), 401
    if id_lembrete:
        return deletar_lembrete_id(id_lembrete, status[0])
    return jsonify({"error": "ID do lembrete é necessário"}), 400


@main.route("/atualiza_id/<int:id_lembrete>", methods=["PUT"])
@jwt_required()
def atualiza_lembrete(id_lembrete):
    user = get_jwt_identity()
    if not user:
        return jsonify({"error": "Usuário não autenticado."}), 401
    lembrete = request.get_json() or {}
    if id_lembrete and lembrete.get("titulo") and lembrete.get("descricao") and lembrete.get("status"):
        return atualizar_lembrete_id(id_lembrete, lembrete.get("titulo"), lembrete.get("descricao"), lembrete.get("status"))
    return jsonify({"error": "Dados incompletos"}), 400
