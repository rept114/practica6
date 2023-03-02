
#Define la cantidad de datos de nuestra lista
valor = str(input("¿Cuantos valores deseas ingresar? "))

def palindromo(valor):
    inicio = 0
    fin = len(valor) - 1
    while valor[inicio] == valor[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False


def remover_caracteres_especiales(valor):
    valor = valor.lower()
    valor = valor.replace(" ", "")
    valor = valor.replace("á", "a")
    valor = valor.replace("é", "e")
    valor = valor.replace("í", "i")
    valor = valor.replace("ó", "o")
    valor = valor.replace("ú", "u")
    return valor


cadena_limpia = remover_caracteres_especiales(valor)
es_palindromo = palindromo(cadena_limpia)
if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")



