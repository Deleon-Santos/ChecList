from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config import Base

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    
    lembretes = relationship("Lembrete",back_populates="usuario")
    
class Lembrete(Base):
    __tablename__ = "lembretes"
    id_lembrete = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_hora = Column(DateTime(timezone=True),server_default=func.now())
    status = Column(String)
    user = Column(String, nullable=False)
    area = Column(String)
    prioridade = Column(String)
    
    # FK para users.id_user
    user_rel = Column(
        Integer,
        ForeignKey("users.id_user"),
        nullable=False
    )
    
    # Relacionamento com User
    usuario = relationship(
        "User",
        back_populates="lembretes"
    )
    

