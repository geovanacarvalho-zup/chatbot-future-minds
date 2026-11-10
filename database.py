import sqlite3
from datetime import datetime

DB_NAME = "historico_chat.db"


def inicializar_banco():
    """Cria a tabela de mensagens caso ela ainda não exista."""
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                papel TEXT NOT NULL,
                mensagem TEXT NOT NULL,
                data_hora TEXT NOT NULL
            )
        """
        )
        conexao.commit()


def salvar_mensagem(papel: str, mensagem: str):
    """Grava uma mensagem enviada pelo usuário ou pelo bot."""
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO historico (papel, mensagem, data_hora)
            VALUES (?, ?, ?)
        """,
            (papel, mensagem, data_hora),
        )
        conexao.commit()


def listar_historico():
    """Retorna todas as mensagens armazenadas em ordem cronológica."""
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT papel, mensagem, data_hora FROM historico ORDER BY id ASC"
        )
        return cursor.fetchall()


def limpar_historico():
    """Apaga todas as mensagens salvas para iniciar uma conversa do zero."""
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM historico")
        conexao.commit()