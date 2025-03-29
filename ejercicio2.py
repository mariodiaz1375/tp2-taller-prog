def contar_digitos_2(num):
    cadena = str(abs(num))
    lista = cadena.split(".")
    digitos_enteros = len(lista[0])
    if lista[1] == '0':
        digitos_decimales = 0
        num = int(num)
    else:
        digitos_decimales = len(lista[1])
    return f"\nEl numero {num} tiene {digitos_enteros} digitos enteros y {digitos_decimales} digitos decimales\n"


if __name__ == '__main__':
    num = float(input("Ingrese un numero: "))
    resultado = contar_digitos_2(num)
    print(resultado)
    
