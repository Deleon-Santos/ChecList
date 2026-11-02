from flask import Flask
from flask_cors import CORS
from data.seed import seed
from routes.rotas import main
from config import Base, engine, jwt_config, setup_logging
from model.models import User, Lembrete
import os


app = Flask(__name__)
setup_logging(app)
Base.metadata.create_all(bind=engine)
jwt_config(app)
app.register_blueprint(main)
CORS(app, resources={r"/*": {"origins": "*"}})
seed()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"

    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug
    )
  