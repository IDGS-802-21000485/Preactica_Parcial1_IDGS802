from flask import Flask, request, render_template
import forms
import math

app = Flask(__name__)

@app.route("/")
def calculo():
    return render_template("layout.html")

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

@app.route("/dosPuntos",methods=("GET","POST"))
def alumnos():
    alum_forms=forms.corde(request.form)
    X1 = 0
    X2 = 0

    Y1 = 0
    Y2 = 0

    res = 0
    
    if request.method=='POST':
        X1 = int(alum_forms.X1.data)
        Y1 = int(alum_forms.Y1.data)
        X2 = int(alum_forms.X2.data)
        Y2 = int(alum_forms.Y2.data)

        res = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

    return render_template("distanciaADosPuntos.html", form=alum_forms, res = res)


if __name__ == "__main__":
    app.run(debug=True)
