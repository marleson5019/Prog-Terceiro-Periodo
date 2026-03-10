import atv2

def main():
    qtd = int(input("Quantos números deseja armazenar? "))
    
    
    lista = atv3.armazenar_numeros(qtd)
    
    lista_ordenada = atv3.ordenar_lista(lista)
    
    print("\nLista ordenada:")
    atv3.imprimir_lista(lista_ordenada)


if __name__ == "__main__":
    main()
