from flask import jsonify
from flask_jwt_extended import create_access_token
from bcrypt import checkpw
from config import Session

from model.models import Lembrete, User


def logar(email, senha):
   
    with Session() as session:
        try:
            user = session.query(User).filter_by(email=email).first()
            if not user:
                return jsonify({"error": "Credenciais inválidas."}), 401

            password_matches = checkpw(senha.encode('utf-8'), user.senha.encode('utf-8'))
            if not password_matches:
                return jsonify({"error": "Credenciais inválidas."}), 401

            token = create_access_token(identity=user.id_user)
            return jsonify({
                "status": "ok",
                "user_id": user.id_user,
                "access_token": "Bearer " + token,
                "token_type": "Bearer"
            }), 200
        except Exception as e:
            session.rollback()
            return jsonify({"error": f"Erro ao realizar login: {str(e)}"}), 500
        
def add_lemmbrete(lembrete):
    with Session() as session:
        try:
            new_lembrete = Lembrete(
                titulo=lembrete.get("titulo"),
                descricao=lembrete.get("descricao"),
                data_hora=lembrete.get("data_hora"),
                status=lembrete.get("status"),
                user=lembrete.get("user")
            )
            session.add(new_lembrete)
            session.commit()
            return jsonify({"message": "Lembrete criado com sucesso!"}), 201
        except Exception as e:
            session.rollback()
            return jsonify({"error": f"Erro ao criar lembrete: {str(e)}"}), 500

def pegar_lembretes():
    with Session() as session:
        try: 
            lembretes_ativos = session.query(Lembrete).filter_by(status="ativo").all()
            if not lembretes_ativos:
                return jsonify({"message": "Nenhum lembrete encontrado."}), 404
            return jsonify([{
                                "id": lembretes_ativos.id_lembrete,
                                "titulo": lembretes_ativos.titulo,
                                "descricao": lembretes_ativos.descricao,
                                "data_hora": lembretes_ativos.data_hora,
                                "status": lembretes_ativos.status,
                                "user": lembretes_ativos.user
                             } for lembretes_ativos in lembretes_ativos])
        except Exception as e:

            session.rollback()
            print(lembretes_ativos)
            return jsonify({"error": f"Erro ao pegar lembretes: {str(e)}"}), 500