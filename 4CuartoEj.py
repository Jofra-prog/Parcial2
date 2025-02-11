#4.Desarrollar un algoritmo que calcule el promedio de un arreglo de reales

arre = input("Ingrese los números que desea calcular el promedio, separados por espacios: \n").split()
arre = [float(x) for x in arre]

def promedio(arreglo):
    if not arreglo: 
        return "El arreglo está vacío, no se puede calcular el promedio."
    
    total = sum(arreglo) 
    return total / len(arreglo)  

print(f"El promedio es: {promedio(arre)}")