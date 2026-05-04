from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

respuestas = {
    "horario": "El horario es de lunes a viernes de 6:45 a.m. a 3:00 p.m.",
    "contacto": "Correo: csfn@sanfelipeneribogota.edu.co",
    "historia": "El colegio forma líderes con valores."
}

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json["mensaje"].lower()

    for clave in respuestas:
        if clave in mensaje:
            return jsonify({"respuesta": respuestas[clave]})

    return jsonify({"respuesta": "No tengo esa información aún."})

if __name__ == "__main__":
    app.run(debug=True)