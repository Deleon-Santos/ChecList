from flask import Flask
from flask_cors import CORS
from data.seed import seed
from routes.rotas import main
from config import Base, engine, jwt_config, setup_logging
from model.models import User, Lembrete



app = Flask(__name__)
setup_logging(app)
Base.metadata.create_all(bind=engine)
jwt_config(app)
app.register_blueprint(main)
CORS(app, resources={r"/*": {"origins": "*"}})
seed()

if __name__ == '__main__':
    app.run(debug=True, port=5000)