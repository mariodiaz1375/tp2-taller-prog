import math

def sumar_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma = suma + matriz[i][i]
    return suma

def eliminar_repetidos(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva


def lista_k(matriz):
    lista_k = []
    diagonal = sumar_diagonal(matriz)
    for lista in matriz:
        for num in lista:
            factorial = math.factorial(num)
            if factorial >= diagonal:
                lista_k.append(num)
    lista_k = eliminar_repetidos(lista_k)
    return lista_k


if __name__ == '__main__':
    matriz = [
        [1, 2, 3, 4],
        [4, 5, 6, 2],
        [7, 8, 9, 5],
        [10, 11, 12, 3]
    ]

    lista = [1, 3, 4, 5, 1, 2, 3]
    # lista = eliminar_repetidos(lista)
    # print(lista)
    suma = sumar_diagonal(matriz)
    print(suma)

    listak = lista_k(matriz)
    print(listak)