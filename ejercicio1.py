def contar_digitos(num):
    """Recibe un numero entero y cuenta sus digitos"""
    cantidad = 0
    num = abs(num)
    if num == 0:
         return cantidad+1
    while num > 0:
            dig = num%10
            num = num//10
            cantidad += 1
    return cantidad
    

if __name__ == '__main__':
    num = int(input("Ingrese el numero: "))
    digitos = contar_digitos(num)
    print(f"El numero {num} tiene {digitos} digitos")

