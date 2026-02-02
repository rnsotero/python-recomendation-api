# Python Recommendation API 🚀

API simples desenvolvida em Python com FastAPI para recomendar produtos com base nos interesses de um usuário.

Este projeto foi criado com foco em **aprendizado prático**, boas práticas de desenvolvimento de APIs e organização de código, servindo também como **projeto de portfólio**.

---

## 🧠 Objetivo do Projeto

O objetivo desta API é receber dados de um usuário (nome e interesses) e retornar uma lista de recomendações de produtos relacionadas a esses interesses.

Além da funcionalidade, o projeto busca demonstrar:
- Uso de FastAPI
- Validação de dados com Pydantic
- Organização de código em módulos
- Criação de uma API documentada automaticamente
- Boas práticas iniciais com Git

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Git**

---

## 📂 Estrutura do Projeto

python-recomendation-api/
│
├── app/
│ ├── main.py # Arquivo principal da aplicação
│ ├── routes.py # Definição das rotas/endpoints
│ ├── schemas.py # Modelos de dados e validações (Pydantic)
│ └── services.py # Lógica de negócio (recomendações)
│
├── venv/ # Ambiente virtual (não versionado)
├── requirements.txt # Dependências do projeto
├── .gitignore
└── README.md


---

## ▶️ Como Executar o Projeto Localmente

1️ - Criar o ambiente virtual

```bash
python -m venv venv

2️ - Ativar o ambiente virtual

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

3️ - Instalar as dependências
pip install -r requirements.txt

4️ - Executar a aplicação
uvicorn app.main:app --reload


A aplicação ficará disponível em:

http://127.0.0.1:8000

📄 Documentação da API

O FastAPI gera automaticamente a documentação da API.

Swagger UI:
http://127.0.0.1:8000/docs

OpenAPI JSON:
http://127.0.0.1:8000/openapi.json

📌 Exemplo de Uso
Endpoint

POST /recomendacoes

Exemplo de requisição (JSON)
{
  "id": 1,
  "nome": "Renato",
  "interesses": ["tecnologia", "games"]
}

Exemplo de resposta
[
  "teclado mecânico",
  "cadeira gamer",
  "mouse gamer",
  "controle",
  "monitor",
  "headset"
]

✅ Validação de Dados

A API utiliza Pydantic para validar automaticamente os dados enviados pelo cliente.
Caso algum campo obrigatório esteja ausente ou inválido, a aplicação retorna erro 422 - Unprocessable Entity.

🚀 Próximos Passos (Evoluções Futuras)

Persistência de dados com banco de dados

Implementação de autenticação

Regras de recomendação mais avançadas

Testes automatizados

Containerização com Docker

👨‍💻 Autor

Projeto desenvolvido por Renato Sotero
Projeto criado com fins educacionais e para composição de portfólio.
