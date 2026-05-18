
from bcrypt import hashpw, gensalt
from config import Session
from model.models import Lembrete, User


def seed():
    with Session() as session:
        try:
            # Criar um usuário de exemplo
            user = session.query(User).first()
            if user:
                return
            
            user = User(
                nome="João Silva",
                email="joao.silva@gmail.com",
                senha=hashpw("123456".encode('utf-8'), gensalt()).decode('utf-8')
            )
            session.add(user)
            session.commit()

            lembrete = Lembrete(
                titulo="Reunião importante",
                descricao="Discutir o projeto X",
                data_hora="2023-10-01 14:30:00",
                user="João Silva",
                status="ativo"
            )
            session.add(lembrete)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Erro ao criar lembrete: {str(e)}")