from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à API Flask!"

@app.route('/saudacao/<nome>', methods=['GET'])
def saudacao(nome):
    return jsonify({'mensagem': f'Olá, {nome}!'})

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    numero1 = dados.get('numero1')
    numero2 = dados.get('numero2')
    if numero1 is None or numero2 is None:
        return jsonify({'erro': 'Os números não foram fornecidos corretamente.'}), 400
    resultado = numero1 + numero2
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
