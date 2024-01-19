listaNumer = []
canNumero = int(input("Cuantos numeros vas a meter: "))

for i in range(canNumero):
    c = int(input("Cuales van a ser: "))
    listaNumer.append(c)

pares = []
impares = []
repetidos = []

for numero in listaNumer:
    if listaNumer.count(numero) > 1 and numero not in repetidos:
        repetidos.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Muestra los resultados
print("Números pares:", pares)
print("Números impares:", impares)
print("Números que se repiten más de una vez:", repetidos)
