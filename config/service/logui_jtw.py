
from flask_jwt_extended import create_access_token
from flask import jsonify
import jwt


def logar(email=str, senha=str):
    token =  create_access_token(identity=str(email))
    return jsonify({"token": token}), 200
    return jsonify({"error": "Dados incompletos"}), 400