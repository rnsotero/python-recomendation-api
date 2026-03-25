# 🚀 Recommendation API

[![Python](https://img.shields.io/badge/Python-3.10+-blue)]
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)]
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)]

Uma **API de recomendação** desenvolvida com FastAPI que sugere produtos com base nos interesses e histórico de compras do usuário.

👉 Projeto focado em **backend, APIs REST e boas práticas de arquitetura**

---

## 🌐 🔥 Live API (em breve)

> 🚀 Em deploy no Render

Após deploy:

```
https://python-recomendation-api.onrender.com/docs
```

---

## 📌 Funcionalidades

* 🔎 Sistema de recomendação baseado em interesses
* 👤 Cadastro de usuário no banco de dados
* 📊 Persistência com SQLite + SQLAlchemy
* ⚡ API REST com FastAPI
* 📄 Documentação automática (Swagger)
* 🧠 Lógica de recomendação customizada
* 🩺 Endpoint de health check

---

## 🧠 Como funciona a recomendação

A API analisa:

* interesses do usuário
* histórico de compras

E retorna sugestões como:

| Entrada    | Saída                     |
| ---------- | ------------------------- |
| tecnologia | teclado mecânico, monitor |
| games      | cadeira gamer, headset    |
| notebook   | mouse, suporte notebook   |

---

## 🛠️ Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

---

## 📂 Estrutura do projeto

```
app/
│
├── main.py
├── routes.py
├── service.py
│
├── schemas/
│   └── usuario.py
│
├── database/
│   ├── database.py
│   ├── models.py
│   └── deps.py
```

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

```
git clone https://github.com/rnsotero/python-recomendation-api.git
```

### 2. Acesse a pasta

```
cd python-recomendation-api
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Execute a API

```
python -m uvicorn app.main:app --reload
```

---

## 🌐 Acessar a API

Swagger:

```
http://localhost:8000/docs
```

---

## 🧪 Exemplo de requisição

### POST `/api/recomendar`

```json
{
  "nome": "Renato",
  "interesses": ["tecnologia", "games"],
  "historico_compras": ["notebook"]
}
```

---

## 📦 Exemplo de resposta

```json
{
  "success": true,
  "data": {
    "id": 1,
    "usuario": "Renato",
    "recomendacoes": [
      "mouse",
      "suporte notebook"
    ]
  }
}
```

---

## 🩺 Health Check

```
GET /api/health
```

Resposta:

```json
{
  "status": "ok"
}
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com foco em:

* construção de APIs REST
* organização de código backend
* integração com banco de dados
* simulação de sistemas reais de recomendação

---

## 📚 Aprendizados

* estruturação de APIs com FastAPI
* uso de SQLAlchemy para persistência
* validação de dados com Pydantic
* separação de responsabilidades (routes, service, models)
* criação de endpoints profissionais

---

## 🚀 Melhorias futuras

* 🔐 Autenticação com JWT
* 🧠 Recomendação com Machine Learning
* 🌐 Deploy com banco externo (PostgreSQL)
* 📊 Logs estruturados
* 🧪 Testes automatizados

---

## 🤝 Contribuições

Contribuições são bem-vindas!

---

## 📄 Licença

MIT

---

💡 Projeto com foco em evolução contínua e boas práticas de backend.
