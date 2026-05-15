from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager # type: ignore

SQLALCHEMY_DATABASE_URL = "sqlite:///./checklist.db"        

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

jwt = JWTManager()

def jwt_config(app):
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
    app.config['JWT_HEADER_NAME'] = "Autorização"
    jwt.init_app(app)
  
