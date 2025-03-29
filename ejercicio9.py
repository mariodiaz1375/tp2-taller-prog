def mayor_de_lista(lista, num):
    es_mayor = True
    for elemento in lista:
        if num >= elemento:
            es_mayor = True
        else:
            es_mayor = False
            return es_mayor
    if es_mayor:
        return es_mayor
    
def menor_de_lista(lista, num):
    es_menor = True
    for elemento in lista:
        if num <= elemento:
            es_menor = True
        else:
            es_menor = False
            return es_menor
    if es_menor:
        return es_menor
    

def lista_columna(matriz, j):
    # convierte una columna de una matriz en una lista, pasando el indice de la columna
    columna = []
    for i in range(len(matriz)):
        columna.append(matriz[i][j])
    return columna

def es_silla(matriz, i, j):
    fila = matriz[i]
    columna = lista_columna(matriz, j)
    mayor_fila = mayor_de_lista(fila, matriz[i][j])
    menor_colum = menor_de_lista(columna, matriz[i][j])
    if mayor_fila and menor_colum:
        return True
    else:
        return False

if __name__ == '__main__':

    matriz2 = [
        [4, 5, 6],
        [7, 8, 9],
        [3, 2, 1],
        [10, 11, 12],
        [4, 2, 3]
    ]


    # lista = [3,5,4,2,41,1231,25,426,234,123]
    # print('es mayor ?')
    # mayor = mayor_de_lista(lista, 1231)
    # print(mayor)
    # print('es menor ?')
    # menor = menor_de_lista(lista, 6)
    # print(menor)

    # columna = lista_columna(matriz2, 0)
    # print(columna)
    silla = es_silla(matriz2, 2, 0)
    print(f'Numero: {matriz2[2][0]}')
    print(f'Es punto silla? {silla}')