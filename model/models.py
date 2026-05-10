from datetime import date

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    
class Lembrete(Base):
    __tablename__ = "lembretes"
    id_lembrete = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_hora = Column(Integer, nullable=False)
    status = Column(String, default="pendente")
    user=Column(Integer, ForeignKey("users.id_user"))
    
    user_rel = relationship("User", backref="lembretes")

