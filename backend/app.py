from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_connection
from models import insertar_jarabe,obtener_jarabes, actualizar_jarabe,eliminar_jarabe

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    connection = get_connection()
    if connection:
        connection.close()
        return jsonify({"mensaje": "Conexion a MySQL exitosa"}), 200
    else:
        return jsonify({"error": "Fallo la conexion a MySQL"}), 500

@app.route('/jarabes', methods=['POST'])
def crear_jarabe():
    print(">> POST /jarabes recibido")
    data = request.get_json()
    print(" Recibido en POST /jarabes:", data)
    nombre = data.get("nombre")
    ingredientes = data.get("ingredientes")
    descripcion = data.get("descripcion")

    if not nombre or not ingredientes:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    resultado = insertar_jarabe(nombre, ingredientes, descripcion)
    return jsonify(resultado)

@app.route('/jarabes', methods=['GET'])
def listar_jarabes():
    resultado = obtener_jarabes()
    return jsonify(resultado)

@app.route('/jarabes/<int:id>', methods=['PUT'])
def modificar_jarabe(id):
    data = request.get_json()
    nombre = data.get("nombre")
    ingredientes = data.get("ingredientes")
    descripcion = data.get("descripcion")

    if not nombre or not ingredientes:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    resultado = actualizar_jarabe(id, nombre, ingredientes, descripcion)
    return jsonify(resultado)

@app.route('/jarabes/<int:id>', methods=['DELETE'])
def borrar_jarabe(id):
    resultado = eliminar_jarabe(id)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
