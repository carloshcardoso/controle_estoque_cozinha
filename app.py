
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Aqui você incluiria o código para buscar itens do banco de dados
    return 'Página inicial do controle de estoque'

@app.route('/estoque', methods=['GET', 'POST'])
def estoque():
    if request.method == 'POST':
        # Aqui você incluiria o código para adicionar, atualizar ou remover itens
        return redirect(url_for('index'))
    return 'Formulário para adicionar, atualizar ou remover itens do estoque'

if __name__ == '__main__':
    app.run(debug=True)
