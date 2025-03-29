from crear_vector import crear_vector_entero

def crear_matriz_cuadrada(filas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_entero(filas))
    return matriz

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_entero(columnas))
    return matriz

if __name__ == '__main__':
    print('matriz cuadrada: ')
    matriz_c = crear_matriz_cuadrada(5)
    for fila in matriz_c:
        print(fila)

    print('la otra xd')
    matriz = crear_matriz(5,3)
    for fila in matriz:
        print(fila)
    