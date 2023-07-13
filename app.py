from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulação de dados de exemplo
    data = {
        'id': 1,
        'name': 'Exemplo',
        'description': 'Isso é um exemplo de API REST com Flask'
    }

    # Retorna os dados como resposta em formato JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000/api/data