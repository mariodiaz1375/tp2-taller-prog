from ejercicio9 import lista_columna 


# def listas_iguales(lista1, lista2):
#     iguales = True
#     if len(lista1) == len(lista2):
#         for i in range(len(lista1)):
#             if lista1[i] == lista2[i]:
#                 pass
#             else:
#                 iguales = False
#                 break
#         return iguales
#     else:
#         iguales = False
#         return iguales
    

def matriz_simetrica(matriz):
    es_simetrica = True
    for i in range(len(matriz)):
        if matriz[i][i:] == lista_columna(matriz, i)[i:]:
            pass
        else:
            es_simetrica = False
            break
    return es_simetrica

    

if __name__ == '__main__':
    
    lista1 = [1,2,3,4]
    lista2 = [1,2,2,4,6]

    matriz = [
        [1, 4, 7, 10],
        [4, 5, 6, 11],
        [7, 6, 9, 12],
        [10, 11, 12, 3]
    ]

    print(matriz_simetrica(matriz))