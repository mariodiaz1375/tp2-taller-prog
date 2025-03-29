def invertir_con_aux(lista):
    cont = 0
    aux = lista
    for num in aux[::-1]:
        lista[cont] = num
        cont += 1
    return lista


def invertir_sin_aux(lista):
    contador = len(lista)
    lista_invertida = []
    while contador > 0:
        contador -= 1
        lista_invertida.append(lista[contador])
    return lista_invertida

if __name__ == '__main__':
    numeros = [11,24,46,-90,145,21,279,1,29,-7]
    print(numeros)
    invertida = invertir_sin_aux(numeros)
    print(invertida)
    invertida2 = invertir_con_aux(numeros)
    print(invertida2)
