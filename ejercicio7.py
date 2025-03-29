def promedio_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    promedio = suma/len(lista)
    return promedio


def promedio_fila(matriz):
    for i in range(len(matriz)):
        promedio = promedio_lista(matriz[i])
        print(f'El promedio de la fila {i} es {promedio}')

        
def promedio_columna(matriz):
    for i in range(len(matriz[0])):
        columna = []
        for lista in matriz:
            columna.append(lista[i])
        promedio = promedio_lista(columna)
        print(f'el promedio de la columna {i} es {promedio}')


if __name__ == '__main__':
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    matriz2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [4, 2, 3]
    ]

    matriz3 = [
        [1, 2, 3, 4],
        [4, 5, 6, 2],
        [7, 8, 9, 5],
        [10, 11, 12, 3]
    ]

    matriz4 = [
        [1, 2, 3, 4, 1],
        [4, 5, 6, 2, 3],
        [7, 8, 9, 5, 1],
        [10, 11, 12, 3, 4]
    ]

    print(matriz)
    promedio_fila(matriz)
    promedio_columna(matriz)
    print('\nmatriz 2')
    promedio_columna(matriz2)
    print('\nmatriz 3')
    promedio_columna(matriz3)
    print('\nmatriz 4')
    promedio_columna(matriz4)