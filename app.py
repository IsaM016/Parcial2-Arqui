from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Usa la ruta /factorial/<numero> para calcular el factorial."


def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact


@app.route('/factorial/<int:num>', methods=['GET'])
def calcular_factorial(num):
    fact = factorial(num)

    if fact is None:
        return jsonify({"error": "No se puede calcular el factorial de un número negativo"}), 400

    etiqueta = "par" if fact % 2 == 0 else "impar"

    respuesta = {
        "numero_recibido": num,
        "factorial": fact,
        "etiqueta": etiqueta
    }

    return jsonify(respuesta)


if __name__ == '__main__':
    app.run(debug=True)
