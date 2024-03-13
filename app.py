from flask import Flask, render_template, request, redirect, url_for, url_quote
import db

app = Flask(__name__)

@app.route('/')
def index():
    itens_estoque = db.obter_itens_estoque()
    return render_template('index.html', itens=itens_estoque)

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