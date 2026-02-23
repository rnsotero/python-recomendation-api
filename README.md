📌 Python Recommendation API

API REST desenvolvida em Python com FastAPI, responsável por gerar recomendações de produtos com base em interesses e histórico de compras do usuário.

O projeto foi construído com foco em:

boas práticas

validação de dados

persistência em banco

testes automatizados

🚀 Tecnologias utilizadas

Python 3.11

FastAPI

Pydantic

SQLAlchemy

SQLite

Pytest

Uvicorn

🧠 Lógica de recomendação

Caso o usuário possua histórico de compras, as recomendações são baseadas nesse histórico

Caso contrário, são usadas as preferências/interesses

O sistema evita recomendações duplicadas

As regras são facilmente extensíveis

📂 Estrutura do projeto
app/
 ├── main.py        # Inicialização da API
 ├── routes.py      # Rotas HTTP
 ├── service.py     # Regras de negócio
 ├── schemas/       # Validação com Pydantic
 ├── database/      # SQLite + SQLAlchemy
tests/
 └── test_recomendacoes.py

▶️ Como executar o projeto
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload


Acesse:

http://127.0.0.1:8000/docs

🧪 Executar os testes
pytest

📈 Próximas evoluções planejadas

Autenticação de usuários

Regras de recomendação mais avançadas

Cache e performance

Containerização com Docker