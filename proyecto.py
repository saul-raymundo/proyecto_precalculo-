"""
debemos crear un proyecto de python que nos ayude a calcular el area total de una figura en el plano cartesiano, donde las 
coordenadas nos los dara el usuario, debemos calcular el area total de las cuatro secciones de un plano cartesiano, 
y debemos mostrar la figura que se llega a crear en el plano cartesiano.
"""
import matplotlib.pyplot as plt
from shapely.geometry import * 

i= 0
arrib = ("*".ljust(50,"*"))
print(arrib)
while True:
    print("*"+ " " * 49 + "*")
    i +=1
    if i == 2:
        text = "BIENVENIDO".center(47)
        print("*",text,"*")
        forma = ("*"+ " " * 49 + "*")
        print(forma+'\n'+ forma+"\n"+arrib)
        break

matrices = {"A":[],"B":[],"C":[],"D":[]}
for name,lista in matrices.items():
    while True:
        dato = input(f"ingrese coordenadas de matriz {name}: ")
        if dato == "":
            break
        valores = dato.split(",")
        tupae = (int(valores[0]),int(valores[1]))
        lista.append(tupae)
        print(f"valor ingresados de {name}: ",lista)



    