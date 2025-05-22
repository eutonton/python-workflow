from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mensagem', methods=['GET'])
def get_mensagem():
    return jsonify({'mensagem': 'Olá, esta é uma mensagem via GET!'})

@app.route('/mensagem', methods=['POST'])
def post_mensagem():
    dados = request.get_json()
    mensagem = dados.get('mensagem', '')
    return jsonify({'mensagem_recebida': mensagem, 'status': 'Mensagem recebida com sucesso!'})

if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    app.run(debug=True)
