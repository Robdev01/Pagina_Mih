from flask import Flask
from flask_cors import CORS
from src.pedidos.router import pedidos_bp
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Inicialização da aplicação Flask
app = Flask(__name__)
CORS(app)

# Registra os Blueprints
app.register_blueprint(pedidos_bp, url_prefix='/api')

# Roda o servidor Flask simples
if __name__ == '__main__':
    print("Servidor rodando em http://0.0.0.0:5002")
    app.run(host='0.0.0.0', port=5002, debug=True)
