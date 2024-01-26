from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def calculo():
    return render_template("calculo.html")

@app.route("/operacion", methods=("GET", "POST"))
def res():
    resultado = None
    operacion = None

    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        ejemplo = int(request.form.get("sta"))

        if ejemplo == 1:
            resultado = num1 + num2
            operacion = "Suma"
        elif ejemplo == 2:
            resultado = num1 - num2
            operacion = "Resta"
        elif ejemplo == 3:
            resultado = num1 * num2
            operacion = "Multiplicación"
        elif ejemplo == 4:
            resultado = num1 / num2
            operacion = "División"

    return render_template("calculo.html", resultado=resultado, operacion=operacion)

if __name__ == "__main__":
    app.run(debug=True)
