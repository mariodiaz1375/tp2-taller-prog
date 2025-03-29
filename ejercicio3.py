def contar_compuestos(lista):
    compuestos = []
    for num in lista:
        divisores = 0
        for i in range(1,num+1):
            if num%i == 0:
                divisores += 1
        if divisores > 2:
            compuestos.append(num)
    return compuestos

if __name__ == '__main__':
    numeros = [11,24,46,90,145,21,279,1,29,7, 9]
    compuestos = contar_compuestos(numeros)
    print(compuestos)
        