from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

import logging
from logging.handlers import RotatingFileHandler
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./checklist.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

jwt = JWTManager()

logger = logging.getLogger("checList")


def setup_logging(app, log_file_path=None):

    if log_file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(
            base_dir,
            "logs",
            "app.log"
        )

    os.makedirs(
        os.path.dirname(log_file_path),
        exist_ok=True
    )

    handler = RotatingFileHandler(
        log_file_path,
        maxBytes=10 * 1024 * 1024,
        backupCount=5
    )

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s"
    )

    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(handler)

    app.config["PROPAGATE_EXCEPTIONS"] = False


def jwt_config(app):

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY"
    )

    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    app.config["JWT_HEADER_NAME"] = "Authorization"
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False

    jwt.init_app(app)