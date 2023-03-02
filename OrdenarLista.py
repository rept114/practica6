#Crear una lista
acumulado = []

#Define la cantidad de datos de nuestra lista
valor = int(input("¿Cuantos valores deseas ingresar? "))

#¿Que valores son?
for i in range(1, valor + 1):
    insert = int(input("Ingresa el valor #{0}: ".format(i)))
    acumulado.append(insert)

#Funcion ordenar max
def ordenar_max(acumulado):
    for x in range(len(acumulado)):
        for y in range(len(acumulado)):
            if acumulado[x] > acumulado[y]:
                temp = acumulado[x]
                acumulado[x] = acumulado[y]
                acumulado[y] = temp
    print("Lista ordenada", end=": ")
    for it in range(len(acumulado)):
        print(acumulado[it], end=", ")
    print("Fin!")
    
def ordenar_min(acumulado):
    for i in range(len(acumulado)):
        for m in range(len(acumulado)):
            if acumulado[i] < acumulado[m]:
                temp = acumulado[m]
                acumulado[m] = acumulado[i]
                acumulado[i] = temp
    print("Lista ordenada", end=": ")
    for it in range(len(acumulado)):
        print(acumulado[it], end=", ")
    print("Fin!")

#¿Qué quiero hacer?
print("""
      \nSelecciona una de las siguientes opciones
      -------------------------------------------
      1)Ordenar de mayor a menor
      2)Ordenar de menor a mayor
      -------------------------------------------
      """)
selec = int(input("Selecciona una opcion: "))
if selec == 1:
    ordenar_max(acumulado)
if selec == 2:
    ordenar_min(acumulado)
else:
    print("Error de sintaxis, valor no corresponde a lo dado")