from flask import jsonify

from config import Session, Base
from model.models import Lembrete

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
        except Exception as e:
            session.rollback()
            

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