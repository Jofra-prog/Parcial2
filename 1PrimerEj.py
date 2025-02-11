#1.Desarrollar un programa que determine si en una lista existen elementos repetidos o no.
#Extra tkinter

import tkinter as tk
from tkinter import messagebox

def lis_sinrep():
    lista1 = entry.get().split()
    sin_rep = set(lista1)
    if len(lista1) == len(sin_rep):
        messagebox.showinfo("Resultado", "La lista no tiene elementos repetidos")
    else:
        messagebox.showinfo("Resultado", f"La lista tiene elementos repetidos. Lista sin repeticiones: {list(sin_rep)}")    

root = tk.Tk()
root.title("Verificador de Listas")#Creo ventana principal

label = tk.Label(root, text="Ingrese la lista de elementos separados por espacios:")
label.pack(pady=5)#Etiqueta de instrucción

entry = tk.Entry(root, width=50)
entry.pack(pady=5)#Campo de entrada

button = tk.Button(root, text="Verificar", command=lis_sinrep)
button.pack(pady=5)#Botón para verificar

root.mainloop()#Ejecutar la aplicación
