from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Ultraman - Volume 16',
        'autor': 'Shimoguchi, Tomohiro; Shimizu, Eiichi'
    },
    {
        'id': 2,
        'título': 'Mo Dao Zu Shi: Comics - Volume 01',
        'autor': 'Mo Xiang Tong Xiu'     
    },
    {
        'id': 3,
        'título': 'Akira - Vol. 06',
        'autor': 'Katsuhiro Otomo'
    }
]

@app.route('/livros',methods=['GET'])

def obter_livros():

    return jsonify(livros)

@app.route('/livros/<int:id>',
            methods=['GET'])

def obter_livros_id(id):

    for livro in livros:

        if livro.get('id') == id:

            return jsonify(livro)

@app.route('/livros',methods=['POST'])

def Add_novo_livro():

    novo_livro = request.get_json()

    livros.append(novo_livro)

    return jsonify(novo_livro)

@app.route('/livros/<int:id>',
            methods=['PUT'])

def editar_livros(id):

    livro_editado = request.get_json()

    for indice,livro in enumerate(livros):

        if livro.get('id') == id:

          livros[indice].update(livro_editado)

          return jsonify(livros[indice])

@app.route('/livros/<int:id>',methods=['DELETE'])

def excluir_livro(id):
    
    for indice,livro in enumerate(livros):
        
        if livro.get('id') == id:
        
            del livros[indice]

        return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)