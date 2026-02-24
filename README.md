# TaskFlow 🚀

TaskFlow é um gerenciador de tarefas web desenvolvido como projeto da disciplina de DevOps.

## 🎯 Objetivo

Aplicar boas práticas de:
- Versionamento com Git
- Conventional Commits
- Pull Requests
- Code Review
- Estratégia de Branching
- Documentação de API

## 🛠 Tecnologias

### Backend
- FastAPI
- SQLite (dev)
- PostgreSQL (produção)

### Frontend
- HTML
- CSS
- JavaScript

## 🌿 Estratégia de Branching

- main → versão estável
- develop → integração
- feature/* → novas funcionalidades

## 📦 Como rodar o projeto

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
