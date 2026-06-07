from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager # type: ignore

import logging
from logging.handlers import RotatingFileHandler
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./checklist.db"

# Disable SQLAlchemy echo to avoid logging SQL statements/parameters
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

jwt = JWTManager()

# Application logger (writes to a rotating file). Use logger.exception() in code
# to record full tracebacks to logs while returning generic messages to clients.
logger = logging.getLogger("checList")

def setup_logging(app, log_file_path=None):
    if log_file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(base_dir, '..', 'logs', 'app.log')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    handler = RotatingFileHandler(log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)

    # Avoid propagating internal exceptions to the client
    app.config['PROPAGATE_EXCEPTIONS'] = False

def jwt_config(app):
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui_que_nem_eu_sei_mas_'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
    app.config['JWT_HEADER_NAME'] = "Authorization"
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    jwt.init_app(app)

