#2.Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o mas vocales.
#Si en la cadena existe debe imprimir y si no existe debe imprimir no existe

def contiene_dos_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in palabra if letra in vocales)
    return contador >= 2#cuenta si hay vocales y retorna un booleano

def verificar_lista(lista):
    resultado = [palabra for palabra in lista if contiene_dos_vocales(palabra)]
    if resultado:
        print(f"Palabras con dos o más vocales: {resultado}")
    else:
        print("No existe ninguna palabra con dos o más vocales.")


lista = input("Ingrese palabras separadas por espacios: \n").split()
verificar_lista(lista)