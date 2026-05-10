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
            