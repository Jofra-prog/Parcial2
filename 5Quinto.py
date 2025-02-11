#5.Desarrollar un algoritmo que determine la mediana de un arreglo de enteros. 
# La mediana es el numero que queda en la mitad del arreglo despues de ser ordenado


med = input("Ingrese el arreglo que desea hayar la mediana separados por espacios: \n").split()

def hayar_med (arreglo):
    listasort = sorted(arreglo)
    lar = len(listasort)
    print("La mediana es: \n",listasort[int(lar/2)])

hayar_med(med)