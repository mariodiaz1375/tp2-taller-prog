def insertar_k(lista, k):
    lista_2 = []
    for num in lista:
        if num%k == 0:
            lista_2.append(num)
            lista_2.append(k)
        else:
            lista_2.append(num)
    return lista_2

numeros = [11,24,46,91,145,21,279,1,29,7,188,519,328]
lista_2 = insertar_k(numeros, 2)
print(lista_2)


        
