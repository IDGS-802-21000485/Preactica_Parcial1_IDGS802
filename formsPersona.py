from wtforms import Form
from wtforms import StringField, RadioField

class Persona(Form):
    nombre = StringField("Nombre")
    apellidoP = StringField("Apellido Paterno")
    apellidoM = StringField("Apellido Materno")
    diaN = StringField("Dia")
    mesN = StringField("Mes")
    annioN = StringField("Año")
    genero = RadioField('Sexo', choices=[('Hombre', 'Hombre'), ('Mujer','Mujer')])