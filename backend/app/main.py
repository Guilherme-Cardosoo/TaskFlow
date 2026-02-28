from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Gerenciador de Tarefas")

# --- BANCO DE DADOS (Configuração Inicial) ---
def init_db():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            concluida BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False

@app.get("/")
def home():
    return {"mensagem": "API de Tarefas Ativa!"}

@app.post("/tarefas/")
def criar_tarefa(tarefa: Tarefa):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, concluida) VALUES (?, ?)", 
                   (tarefa.titulo, tarefa.concluida))
    conn.commit()
    conn.close()
    return {"status": "Tarefa criada com sucesso!"}

@app.get("/tarefas/")
def listar_tarefas():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return {"tarefas": tarefas}

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    tarefa = cursor.fetchone()
    
    if not tarefa:
        conn.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    conn.close()
    
    return {"status": f"Tarefa {tarefa_id} deletada com sucesso!"}