print("="*50)
print("\n Clasificador de Edades\n")
print("="*50) 
print("\nEste programa categorizara cada edad en Menor,Adulto y Mayor")

entrada = input("> Introduce las edades separadas por espacio: ").split()

lista_edades = [int(e) for e in entrada]

def categorizar_edades(edades):
    categorias = [] 
    
    for edad in edades:
        # Requerimiento: if-elif-else para clasificar
        if edad < 18:
            categorias.append("Menor")
        elif edad < 65:
            categorias.append("Adulto")
        else:
            categorias.append("Mayor")
            
    return categorias

resultado = categorizar_edades(lista_edades)

print(resultado)
