from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class corde(Form):
    X1 = StringField("X1")
    Y1 = StringField("Y1")

    X2 = StringField("X2")
    Y2 = StringField("Y2")
    
class dicc(Form):
    palEsp=StringField('Español',[
        validators.DataRequired(message='el compo es requerido'),
        validators.length(min=2, max=10, message='ingresa nombre valido')
    ])
    
    palIng=StringField('Ingles',[
        validators.DataRequired(message='el compo es requerido'),
        validators.length(min=2, max=10, message='ingresa nombre valido')
    ])
    
    lengu = RadioField('Idioma', choices=[('Ingles', 'Ingles'), ('Español','Español')])
    
    bus=StringField('Buscar',[
        validators.DataRequired(message='el compo es requerido'),
        validators.length(min=2, max=10, message='ingresa nombre valido')
    ])