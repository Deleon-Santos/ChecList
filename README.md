# ChecList

API construda com Flask para gerenciamento de lembretes(CRUD) com autenticação JWT, Bcrypt, Docker e documentação Swagger.

## 🚀 Tecnologias Utilizadas

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" title="Python">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="60" title="Flask">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" width="60" title="SQLAlchemy">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="60" title="SQLite">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="60" title="Docker">
</p>

- Python 3.12
- Flask
- SQLAlchemy
- Flask-JWT-Extended
- Flask-CORS
- Passlib (bcrypt)
- SQLite
- Swagger UI
- Docker / Docker Compose

## 📁 Estrutura do projeto

- `run.py` - ponto de entrada da aplicação Flask
- `routes/rotas.py` - rotas da API e rota da documentação
- `controllers/controller.py` - lógica de gerenciamento de usuários e lembretes
- `model/models.py` - modelos SQLAlchemy
- `config/__init__.py` - configuração do banco de dados, JWT e logging
- `data/seed.py` - script de seed para dados iniciais
- `templates/index.html` - interface Swagger UI
- `static/openapi.json` - especificação OpenAPI separada
- `Dockerfile` - imagem Docker da aplicação
- `docker-compose.yml` - orquestração do serviço web

## ⚙️ Requisitos

- Git
- Docker e Docker Compose (se for executar via container)
- Python 3.12 ou superior

## 💻 Como clonar

```bash
git clone <url-do-repositorio> ChecList
cd ChecList
```

## 🐍 Como executar localmente

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python run.py
```

4. Acesse a documentação pelo navegador:

- `http://localhost:5000/`

## 🐳 Como executar com Docker

1. Build da imagem:

```bash
docker compose build
```

2. Subir o serviço:

```bash
docker compose up
```

3. Acesse a aplicação em:

- `http://localhost:5000/`

## 🔧 Necessidades desta aplicação

- Gerenciar lembretes com autenticação segura
- Registrar e autenticar usuários com JWT
- Expor documentação de API clara e interativa
- Executar localmente e em container Docker
- Persistência leve com SQLite

## 📌 Endpoints principais

- `POST /cadastro` - registrar usuário
- `POST /login` - autenticar e receber token JWT
- `POST /lembrete` - criar lembrete (JWT requerido)
- `GET /lembrete` - listar lembretes do usuário (JWT requerido)
- `GET /lembrete_id/<id>` - obter lembrete por ID (JWT requerido)
- `DELETE /deleta_id/<id>` - excluir lembrete (JWT requerido)
- `PUT /atualiza_id/<id>` - atualizar lembrete (JWT requerido)
- `GET /api` - especificação OpenAPI JSON

## 📚 Observações

- A documentação do Swagger está configurada para carregar `static/openapi.json`.
- Caso use Docker, o banco SQLite ficará persistido dentro do container se não for mapeado externamente.
