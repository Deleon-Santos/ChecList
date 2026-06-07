from flask import jsonify
from flask_jwt_extended import create_access_token
from bcrypt import checkpw, hashpw, gensalt
from config import Session, logger
from model.models import Lembrete, User


def novo_user(nome, email, senha):
    with Session() as session:
        try:
            if session.query(User).filter_by(email=email).first():
                return jsonify({"error": "Email já cadastrado."}), 400
            
            hash_senha = hashpw(senha.encode('utf-8'), gensalt()).decode('utf-8')
            novo_user = User(nome=nome, email=email, senha= hash_senha)
            session.add(novo_user)
            session.commit()
            return jsonify({"message": "Usuário criado com sucesso!"}), 201
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao criar novo usuário")
            return jsonify({"error": "Erro interno do servidor."}), 500


def logar(email, senha):
    with Session() as session:
        try:
            user = session.query(User).filter_by(email=email).first()
            if not user:
                return jsonify({"error": "Credenciais  inválidas."}), 401

            password_matches = checkpw(senha.encode('utf-8'), user.senha.encode('utf-8'))
            if not password_matches:
                return jsonify({"error": "Credenciais inválidas."}), 401

            token = create_access_token(identity=user.id_user)
            return jsonify({
                "status": "ok",
                "user_id": user.id_user,
                "access_token": token,
                "token_type": "Bearer"
            }), 200
        
        except Exception:
            logger.exception("Erro ao realizar login")
            return jsonify({"error": "Erro interno do servidor."}), 500


def add_lemmbrete(titulo, descricao, user, status):
    with Session() as session:
        try:
            new_lembrete = Lembrete(
                titulo=titulo,
                descricao=descricao,
                
                status=status,
                user=user
            )
            session.add(new_lembrete)
            session.commit()
            return jsonify({"message": "Lembrete criado com sucesso!"}), 201
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao criar lembrete")
            return jsonify({"error": "Erro interno do servidor."}), 500

def pegar_lembretes():
    with Session() as session:
        try: 
            lembretes_ativos = session.query(Lembrete).filter_by(status="ativo").all()
            if not lembretes_ativos:
                return jsonify({"message": "Nenhum lembrete encontrado."}), 404
            
            return jsonify([{
                                "id": lembretes_ativos.id_lembrete,
                                "tiprint(lembretes_ativos)tulo": lembretes_ativos.titulo,
                                "descricao": lembretes_ativos.descricao,
                                "data_hora": lembretes_ativos.data_hora,
                                "status": lembretes_ativos.status,
                                "user": lembretes_ativos.user
                             } for lembretes_ativos in lembretes_ativos]), 200
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao pegar lembretes")
            return jsonify({"error": "Erro interno do servidor."}), 500


def pegar_lembrete_id(id_lembrete):
    with Session() as session:
        try: 
            lembrete = session.query(Lembrete).filter_by(id_lembrete=id_lembrete).first()
            if not lembrete:
                return jsonify({"message": "Lembrete não encontrado."}), 404
            
            return jsonify({
                                "id": lembrete.id_lembrete,
                                "titulo": lembrete.titulo,
                                "descricao": lembrete.descricao,
                                "data_hora": lembrete.data_hora,
                                "status": lembrete.status,
                                "user": lembrete.user
                             }), 200
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao pegar lembrete por ID")
            return jsonify({"error": "Erro interno do servidor."}), 500
        

def pegar_lembrete_id(id_lembrete):
    with Session() as session:
        try: 
            lembrete = session.query(Lembrete).filter_by(id_lembrete=id_lembrete).first()
            if not lembrete:
                return jsonify({"message": "Lembrete não encontrado."}), 404
            
            return jsonify({
                                "id": lembrete.id_lembrete,
                                "titulo": lembrete.titulo,
                                "descricao": lembrete.descricao,
                                "data_hora": lembrete.data_hora,
                                "status": lembrete.status,
                                "user": lembrete.user
                             }), 200
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao pegar lembrete por ID")
            return jsonify({"error": "Erro interno do servidor."}), 500


def deletar_lembrete_id(id_lembrete):
    with Session() as session:
        try: 
            lembrete = session.query(Lembrete).filter_by(id_lembrete=id_lembrete).first()
            if not lembrete:
                return jsonify({"message": "Lembrete não encontrado."}), 404
            
            session.delete(lembrete)
            session.commit()
            return jsonify({"message": "Lembrete deletado com sucesso!"}), 200
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao deletar lembrete por ID")
            return jsonify({"error": "Erro interno do servidor."}), 500
        

def atualizar_lembrete_id(id_lembrete, titulo, descricao, status):
    with Session() as session:
        try: 
            lembrete = session.query(Lembrete).filter_by(id_lembrete=id_lembrete).first()
            if not lembrete:
                return jsonify({"message": "Lembrete não encontrado."}), 404
            
            lembrete.titulo = titulo
            lembrete.descricao = descricao
            lembrete.status = status
            session.commit()
            return jsonify({"message": "Lembrete atualizado com sucesso!"}), 200
        
        except Exception:
            session.rollback()
            logger.exception("Erro ao atualizar lembrete por ID")
            return jsonify({"error": "Erro interno do servidor."}), 500
