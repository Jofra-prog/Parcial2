#3.Desarrollar un programa que dada dos listas determine que elementos tiene la primera lista que no tenga la segunda lista


lista1 = input("ingrese la primer lista deseada a comparar separada por espacios: \n").split()
lista2 = input("ingrese la segunda lista deseada a comparar separada por espacios: \n").split()

def det_elem1_not_in2(lista1,lista2):
    lol = []
    for x in lista1:
        if x not in lista2:
            lol.append(x)
            
    if len(lol) == 0:
        print("No hay elementos en la primer lista que no esten en la segunda")
    else:
        print(f"Los elementos que hay en la primer lista mas no en la segunda son: {set(lol)}")

det_elem1_not_in2(lista1,lista2)