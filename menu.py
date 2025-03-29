from ejercicio1 import contar_digitos
from ejercicio2 import contar_digitos_2
from ejercicio3 import contar_compuestos
from ejercicio4 import invertir_con_aux, invertir_sin_aux
from ejercicio5 import ejercicio5
from ejercicio6 import insertar_k
from ejercicio7 import promedio_columna, promedio_fila
from ejercicio8 import lista_k
from ejercicio9 import es_silla
from ejercicio10 import matriz_simetrica

from crear_vector import crear_vector_entero, crear_vector_real
from crear_matriz import crear_matriz, crear_matriz_cuadrada


while True:
    try:
        print('**** TRABAJO PRACTICO 2 DE TALLER DE PROGRAMACION ****')
        print('1. Ejercicio 1')
        print('2. Ejercicio 2')
        print('3. Ejercicio 3')
        print('4. Ejercicio 4')
        print('5. Ejercicio 5')
        print('6. Ejercicio 6')
        print('7. Ejercicio 7')
        print('8. Ejercicio 8')
        print('9. Ejercicio 9')
        print('10. Ejercicio 10')
        print('11. Salir')
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:

            try:
                numero = int(input('\nIngrese un numero entero para contar sus digitos: '))
                digitos = contar_digitos(numero)
                print(f'\nEl numero {numero} tiene {digitos} digitos\n')
            except Exception as e:
                print(f'\nOcurrio un error: {e}')
                print('Ingrese solo un numero entero\n')

        elif opcion == 2:

            try:
                numero = float(input('\nIngrese un numero para contar sus digitos: '))
                resultado = contar_digitos_2(numero)
                print(resultado)
            except Exception as e:
                print(f'\nOcurrio un error: {e}')
                print('Ingrese solo un numero\n')

        elif opcion == 3:

            try:
                cantidad = int(input('Ingrese la cantidad de numeros del vector: '))
                vector = crear_vector_entero(cantidad)
                print(f'\nEl vector creado es: {vector}')
                compuestos = contar_compuestos(vector)
                print(f'Este vector tiene los siguientes numeros compuestos: {compuestos}\n')
            except Exception as e:
                print(f'Ocurrio un error: {e}') 

        elif opcion == 4:

            try:
                cantidad = int(input('Ingrese la cantidad de numeros del vector: '))
                vector = crear_vector_entero(cantidad)
                print(f'\nEl vector creado es: {vector}')
                print('\na. Invertirlo usando un vector auxiliar.')
                print('b. Invertirlo sin vector auxiliar.\n')
                opcion4 = input('Ingrese una opcion: ')
                
                if opcion4.lower() == 'a':
                    vector_invertido = invertir_con_aux(vector)
                    print(f'\nEl vector invertido usando auxiliar es: {vector_invertido}\n')
                elif opcion4.lower() == 'b':
                    vector_invertido = invertir_sin_aux(vector)
                    print(f'\nEl vector invertido sin usar auxiliar es: {vector_invertido}\n')
                else:
                    print('\nIngrese una opcion valida\n')
            except ValueError as v:
                print(f'\nOcurrio un error: {v}')
                print('Solo ingrese numeros para la creacion del vector\n')
            except Exception as e:
                print(f'\nOcurrio un error: {v}')
                print('Solo ingrese "a" o "b" para las opciones\n')

        elif opcion == 5:

            try: 
                cantidad = int(input('Ingrese la cantidad de numeros del vector: '))
                vector_a = crear_vector_real(cantidad)
                print(f'\nEl vector creado es: {vector_a}')
                vector_b = ejercicio5(vector_a)
                print(f'\nNumeros con dos digitos pares y al menos dos digitos impares: {vector_b}\n')
            except Exception as e:
                print(f'\nOcurrio un error: {e}')
                print('Solo ingrese numeros para la creacion del vector\n')
        
        elif opcion == 6:

            try:
                cantidad = int(input('Ingrese la cantidad de numeros del vector: '))
                vector = crear_vector_entero(cantidad)
                print(f'\nEl vector creado es: {vector}')
                k = int(input('Ingrese el valor de K: '))
                vector_k = insertar_k(vector, k)
                print(f'El vector con {k} a la derecha de cada multiplo: {vector_k}\n')
            except Exception as e:
                print(f'\nOcurrio un error: {e}\n')

        elif opcion == 7:

            try:
                filas = int(input('Ingrese la cantidad de filas de la matriz: '))
                columnas = int(input('Ingrese la cantidad de columnas de la matriz: '))
                matriz = crear_matriz(filas, columnas)
                print('\nMatriz creada: ')
                for fila in matriz:
                    print(fila)
                print('\nPromedio de filas: ')
                promedio_fila(matriz)
                print('\nPromedio de columnas: ')
                promedio_columna(matriz)
                print('\n')
            except Exception as e:
                print(f'\nOcurrio un error: {e}')
                print('Solo ingrese numeros enteros para filas y columnas\n')

        elif opcion == 8:
            
            try:
                filas = int(input('Ingrese la cantidad de filas de la matriz: '))
                matriz = crear_matriz_cuadrada(filas)
                print('\nMatriz creada: ')
                for fila in matriz:
                    print(fila)
                vector_k = lista_k(matriz)
                print('\nNumeros de la matriz donde su factorial sea mayor o igual a la suma de la diagonal principal:')
                print(f'{vector_k}\n')

            except Exception as e:
                print(f'\nOcurrio un error: {e}')
                print('Solo ingrese numeros enteros para las filas de la matriz\n')
            
        elif opcion == 9:
                
            try:
                filas = int(input('Ingrese la cantidad de filas de la matriz: '))
                columnas = int(input('Ingrese la cantidad de columnas de la matriz: '))
                matriz = crear_matriz(filas, columnas)
                print('\nMatriz creada: ')
                for fila in matriz:
                    print(fila)
                k = int(input('\nIngrese el valor del indice k: '))
                h = int(input('Ingrese el valor del indice h: '))
                print(f'El numero selenccionado es: {matriz[k][h]}')
                silla = es_silla(matriz, k, h)
                print(f'\nEs punto silla?  {silla}\n')
            except Exception as e:
                print(f'\nOcurrio un error: {e}\n')

        elif opcion == 10:
                
            try:
                filas = int(input('Ingrese la cantidad de filas de la matriz: '))
                matriz = crear_matriz_cuadrada(filas)
                print('\nMatriz creada: ')
                for fila in matriz:
                    print(fila)
                simetrica = matriz_simetrica(matriz)
                print(f'\nLa matriz es simetrica?  {simetrica}\n')

            except Exception as e:
                print(f'\nOcurrio un error: {e}')
                print('Solo ingrese numeros enteros para las filas de la matriz\n')
        
        elif opcion == 11:
            break

        else:
            print("Ingrese solo numeros del 1 al 11")

    except Exception as e:
        print('Ingrese un opcion valida')