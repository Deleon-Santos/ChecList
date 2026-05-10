from flask import Flask
from routes.rotas import main
from config import Base, engine
from model.models import User, Lembrete



app = Flask(__name__)
Base.metadata.create_all(bind=engine)
# main = blueprints('main', __name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)