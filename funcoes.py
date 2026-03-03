'''Faça um programa em Python 3.0 (ou versão superior) que:

a) Crie uma função que armazene números inteiros pares positivos (fornecidos via console) em uma lista de números inteiros. O usuário de seu programa poderá informar qualquer número inteiro positivo, mas seu programa armazenará somente os número que forem pares positivos. Esta função não recebe parâmetros e retorna a lista preenchida. Considere que os dados de entrada encerram quando o usuário informar um número inteiro menor ou igual a zero.

b) Crie uma função que imprima números inteiros armazenados em uma lista. Esta função recebe como parâmetro uma lista já preenchida. A impressão deverá seguir o formato:

LISTA[9]=99

...

LISTA[9]=99

onde o número 9 representa a posição do elemento na lista e 99 representa o valor do elemento da lista.

c) Faça o programa principal invocando corretamente as funções a) e b) de modo que o programa principal possua uma lista de números inteiros (usando a função a))  e que esta mesma lista seja impressa usando a função b).

Envie dois arquivos py:

- 1o. arquivo a ser enviado é a aplicação, ou seja, o arquivo py que contém a função principal e sua correta invocação

- 2o. arquivo a ser enviado é o módulo, ou seja, o arquivo py que contém as funções desenvolvidas por vc. 

Marlyson Rodrigues Souza 03/03/2026 '''
def coletar_pares():
    lista = []
    numero = int(input())
    while numero > 0:
        if numero % 2 == 0:
            lista.append(numero)
        numero = int(input())
    return lista


def imprimir_lista(lista):

    for i in range(len(lista)):
        print(f"LISTA[{i}]={lista[i]}")
