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

1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/taskflow.git
cd taskflow
```

2. Criar ambiente virtual

🐧 Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

🪟 Windows (PowerShell)
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Entrar na pasta backend
```bash
cd backend/app
```

4. Instalar dependências
```bash
pip install -r requirements.txt
```

5. Rodar o servidor FastAPI
```bash
uvicorn main:app --reload
```

O servidor rodará em:
```bash
http://127.0.0.1:8000
```

Documentação automática:
```bash
http://127.0.0.1:8000/docs
```
