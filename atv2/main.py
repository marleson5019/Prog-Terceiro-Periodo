import atv2

def main():
    qtd = int(input("Quantos números deseja armazenar? "))
    
    
    lista = meu_modulo.armazenar_numeros(qtd)
    
    lista_ordenada = meu_modulo.ordenar_lista(lista)
    
    print("\nLista ordenada:")
    meu_modulo.imprimir_lista(lista_ordenada)


if __name__ == "__main__":
    main()
