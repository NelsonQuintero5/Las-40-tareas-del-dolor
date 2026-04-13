print("="*50)
print("\nConsultor de notas\n")
print("="*50)

clase = {}

print("\n>> archivo de las notas de clases\n")

# Interfaz de edición
fase_1 = True
while fase_1:
    alumnos = input("Introduzca nombres de alumnos:\n").split()
    notas = input("Por favor introduzca las notas de cada alumno en el mismo orden:\n").split()

    #conversor
    for i in range(len(alumnos)):
        clase[alumnos[i]] = int(notas[i]) 
    
    res1 = input("¿Desea salir de la interfaz inicial si/no?: ").lower()
    if res1 == "si":
        fase_1 = False

#funcion
def evaluar_estudiantes(registro):
    resultados = {}
    for nombre in registro:  
        nota = registro[nombre]  
        if nota >= 60:
         estado = "Aprobado"  
        else:
         estado = "Reprobado"

    resultados[nombre] = [nota, estado]
    return resultados

print(evaluar_estudiantes(clase))