
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect('estoque.db')

@app.route('/')
def index():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT produto, categoria, quantidade, data_validade, valor FROM estoque')
    itens = cursor.fetchall()
    conexao.close()
    # Transforma os itens em uma lista de dicionários para facilitar o acesso pelos nomes das colunas no template
    itens_dict = [{'produto': item[0], 'categoria': item[1], 'quantidade': item[2], 'data_validade': item[3], 'valor': item[4]} for item in itens]
    return render_template('index.html', itens=itens_dict)

@app.route('/estoque', methods=['GET', 'POST'])
def estoque():
    if request.method == 'POST':
        produto = request.form['produto']
        categoria = request.form['categoria']
        quantidade = request.form['quantidade']
        data_validade = request.form['data_validade']
        valor = request.form['valor']
        if 'adicionar' in request.form:
            db.adicionar_item(produto, categoria, int(quantidade), data_validade, float(valor))
        elif 'atualizar' in request.form:
            db.atualizar_item(produto, int(quantidade))
        elif 'remover' in request.form:
            db.remover_item(produto)
        return redirect(url_for('index'))
    return render_template('estoque_form.html')

if __name__ == '__main__':
    app.run(debug=True)
