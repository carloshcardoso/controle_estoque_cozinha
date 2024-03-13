
import sqlite3

def conectar():
    conexao = sqlite3.connect('estoque.db')
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        categoria TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        data_validade TEXT NOT NULL,
        valor REAL NOT NULL
    )
    ''')
    conexao.commit()
    conexao.close()

def adicionar_item(produto, categoria, quantidade, data_validade, valor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO estoque (produto, categoria, quantidade, data_validade, valor)
    VALUES (?, ?, ?, ?, ?)
    ''', (produto, categoria, quantidade, data_validade, valor))
    conexao.commit()
    conexao.close()

def obter_itens_estoque():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM estoque')
    itens = cursor.fetchall()
    conexao.close()
    return itens

def atualizar_item(id, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
    UPDATE estoque SET quantidade = ? WHERE id = ?
    ''', (quantidade, id))
    conexao.commit()
    conexao.close()

def remover_item(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM estoque WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()

# Ao importar este módulo, automaticamente tenta criar a tabela se não existir
criar_tabela()
