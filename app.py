from flask import Flask, request, jsonify
from base_datos import guardar_log
from autenticacion import verificar_token

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def recibir_logs():
    token = request.headers.get('Authorization', '').split(' ')[-1]
    if not verificar_token(token):
        return jsonify({"error": "Token no autorizado"}), 401
    
    log_data = request.json
    guardar_log(log_data)
    return jsonify({"mensaje": "Log recibido con éxito"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
