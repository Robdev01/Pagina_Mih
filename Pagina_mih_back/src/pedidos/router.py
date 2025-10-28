from flask import Blueprint, request, jsonify
from src.pedidos.controller import (controller_create_pedidos_ola,
controller_create_pedido_estoque_melhoria,
controller_create_pedido_b2b_pendentes,
controller_create_pedido_b2b_rede_ok

                        )

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route("/upload/pedidos_ola", methods=["POST"])
def upload_pedidos_ola():
    try:
        data = request.get_json()
        resp, status = controller_create_pedidos_ola(data)
        return jsonify(resp), status
    except Exception as e:
        print("❌ Erro na rota /upload/pedidos_ola:", e)
        return jsonify({"message": "Erro interno no servidor"}), 500

@pedidos_bp.route("/upload/pedidos_estoque_melhoria", methods=["POST"])
def upload_pedidos_estoque_melhoria():
    try:
        data = request.get_json()
        resp, status = controller_create_pedido_estoque_melhoria(data)
        return jsonify(resp), status
    except Exception as e:
        print("❌ Erro na rota /upload/pedidos_estoque_melhoria:", e)
        return jsonify({"message": "Erro interno no servidor"}), 500

@pedidos_bp.route("/upload/pedidos_pendentes", methods=["POST"])
def create_pedido_b2b_pendentes():
    try:
        data = request.get_json()
        resp, status = controller_create_pedido_b2b_pendentes(data)
        return jsonify(resp), status
    except Exception as e:
        print("❌ Erro na rota /upload/pedidos_pendentes:", e)
        return jsonify({"message": "Erro interno no servidor"}), 500

@pedidos_bp.route("/upload/pedidos_b2b_rede_ok", methods=["POST"])
def upload_pedidos_b2b_rede_ok():
    try:
        data = request.get_json()
        resp, status = controller_create_pedido_b2b_rede_ok(data)
        return jsonify(resp), status
    except Exception as e:
        print("❌ Erro na rota /upload/pedidos_b2b_rede_ok:", e)
        return jsonify({"message": "Erro interno no servidor"}), 500

