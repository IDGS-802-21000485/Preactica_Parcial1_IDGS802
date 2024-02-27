from flask import Flask, request, render_template
import forms, formsPersona
import math
from datetime import datetime
from io import open

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


@app.route("/zodiaco",methods=("GET","POST"))
def zodiaco():
    fecha_actual = datetime.now()
    person_form=formsPersona.Persona(request.form)
    nombre = ""
    apellidoP = ""
    apellidoM = ""
    diaN = ""
    mesN = ""
    annioN = ""
    genero = ""
    edad = ""
    zodiaco = ""
    imag = ""
    
    if request.method=='POST':
        nombre = str(person_form.nombre.data)
        apellidoP = str(person_form.apellidoP.data)
        apellidoM = str(person_form.apellidoM.data)
        diaN = int(person_form.diaN.data)
        mesN = int(person_form.mesN.data)
        annioN = int(person_form.annioN.data)
        genero = str(person_form.genero.data)
        signos = ['Mono', 'Gallo', 'Perro', 'Cerdo', 'Rata', 'Buey', 'Tigre', 'Conejo', 'Dragón', 'Serpiente', 'Caballo', 'Cabra']
        ciclo_zodiaco = annioN % 12
        zodiaco = signos[ciclo_zodiaco]
        edad = fecha_actual.year - annioN
        if fecha_actual.month < mesN or (fecha_actual.month == mesN and fecha_actual.day < diaN):
            edad -= 1
        imag = "../static/imgZo/"+zodiaco+".jpg"
    return render_template("Zodiaco.html", genero=genero,Persona=person_form, nombre = nombre, apellidoP = apellidoP,apellidoM = apellidoM, annioN = annioN,diaN=diaN,mesN=mesN, edad = edad, zodiaco = zodiaco, imag = imag)

@app.route("/diccionarioEntra",methods=("GET","POST"))
def diccionario():
    dicc=forms.dicc(request.form)
    ing = None
    esp = None
    trad = None
    idi = None
    
    if request.method=='POST':
        p1 = str(dicc.palEsp.data.lower())
        p2 = str(dicc.palIng.data.lower()) 
        
        archivo_texto=open('dic.txt','a')       
        archivo_texto.write('\n'+p1+" "+p2)
        archivo_texto.close()
        

    return render_template("diccionario.html",dicc=dicc)

@app.route("/diccionarioBuscar",methods=("GET","POST"))
def diccionarioBusca():
    dicc=forms.dicc(request.form)
    ing = None
    esp = None
    trad = None
    idi = None
    
    if request.method=='POST':
        p1 = (dicc.lengu.data)
        bus = (dicc.bus.data.lower())
        
        archivo_texto=open('dic.txt','r')
        
        for linea in archivo_texto:
            idi = linea.strip().lower().split()
            print(p1 == "Ingles")
            if (p1 == "Ingles" and idi[0] == bus):
                print("Entro el ingles")
                trad = idi[1]
                print(trad)
            elif (p1 == "Español" and idi[1] == bus):
                print("Entro el español")
                trad = idi[0]
                print("De aqui"+trad)
            if(trad == None):
                trad="No esta dentro del diccionario"
        archivo_texto.close()
    return render_template("diccionario.html",dicc=dicc,trad=trad)


if __name__ == "__main__":
    app.run(debug=True)
    