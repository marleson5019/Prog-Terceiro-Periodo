def armazenar_numeros(qtd):
    lista = []
    for i in range(qtd):
        valor = int(input(f"Digite o {i+1}º número real: "))
        lista.append(valor)
    return lista


def ordenar_lista(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def imprimir_lista(lista):
    for i, valor in enumerate(lista):
        print(f"LISTA[{i}]={valor}")
