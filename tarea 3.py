print("="*50)
print("\n localizador de valor maximo de na lista\n")
print("="*50) 
print()

entrada = input(">introduzca su lista de numeros por favor:\n").split()

lista = [int (i)for i in entrada]

def encontrar_maximo(secuencia):

    maximo = secuencia[0]
    
    for numero in secuencia:
        
        if numero > maximo:
            maximo = numero

    return maximo

resultado = encontrar_maximo(lista)

print(f"\nEl número mayor encontrado es: {resultado}")