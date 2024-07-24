from flask import Flask, jsonify, request
from db import conectar_banco

app = Flask(__name__)


## GET EM TODOS OS FILMES
@app.route('/filmes', methods=['GET'])
def busca_filmes():
    conn = conectar_banco()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM filmes')
    filmes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(filmes)


## GET NO ID
@app.route('/filmes/<int:id>', methods=['GET'])
def busca_filme_id(id):
    conn = conectar_banco()
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM filmes WHERE id = %s'
    cursor.execute(query, (id,))
    filme = cursor.fetchone()
    cursor.close()
    conn.close()
    if filme:
        return jsonify(filme)
    else:
        return jsonify({'message': 'Filme não encontrado'}), 404


## POST NO FILME
@app.route('/filmes', methods=['POST'])
def cria_filme():
    data = request.json
    nome = data['nome']
    autor = data['autor']
    streaming = data['streaming']

    # Criação no banco
    conn = conectar_banco()
    cursor = conn.cursor()
    query = 'INSERT INTO filmes (nome, autor, streaming) VALUES (%s, %s, %s)'
    cursor.execute(query, (nome, autor, streaming))

    conn.commit()
    filme_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({'id': filme_id, 'nome': nome, 'autor': autor, 'streaming': streaming}), 201
