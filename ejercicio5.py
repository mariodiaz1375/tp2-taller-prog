def ejercicio5(lista):
    lista_b = []
    for num in lista:
        aux = abs(int(num))
        dig_par = 0
        dig_impar = 0
        while aux > 0:
            dig = aux%10
            aux = aux//10
            if dig%2 == 0:
                dig_par += 1
            else:
                dig_impar += 1
        if dig_par == 2 and dig_impar >= 2:
            lista_b.append(num)
    return lista_b

numeros = [-3676.073, 24713.567, 1237187238.7565645, 1112345123, 12312.765]
resultado = ejercicio5(numeros)
print(resultado)
