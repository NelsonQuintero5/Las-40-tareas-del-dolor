print("0"*50)
print("\nDectector de numeros primos\n")
print("="*50)
print("")
print("\n>>por favor introduzca un solo numero:\n")

entrada = int(input("Ingresa un número para verificar: "))

def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False 
    
    return True # Si terminó el bucle sin encontrar divisores, es primo

if es_primo(entrada):
    print(f"El {entrada} es un número primo.")
else:
    print(f"El {entrada} NO es un número primo.")
