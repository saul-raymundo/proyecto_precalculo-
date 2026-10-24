"""
debemos crear un proyecto de python que nos ayude a calcular el area total de una figura en el plano cartesiano, donde las 
coordenadas nos los dara el usuario, debemos calcular el area total de las cuatro secciones de un plano cartesiano, 
y debemos mostrar la figura que se llega a crear en el plano cartesiano.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
from sympy.geometry import * 
from matplotlib.ticker import MultipleLocator
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
#pedir datos al usuario y el programa se encarga de agregarlos a un dicionario de listas
matrices = {"A":[],"B":[],"C":[],"D":[]}
for name,lista in matrices.items():
    #con el ciclo while el usuario puede ingresar las cordenadas que desee.
    while True:
        dato = input(f"ingrese coordenadas de matriz {name}: ")
        if dato == "":
            break # cuando el usuario deje un espacio en blanco pasa a la siguiente matriz.
        valores = dato.split(",")
        tupae =(float(valores[0]),float(valores[1]))
        lista.append(tupae)
        print(f"valor ingresados de {name}: ",lista)

coor = []
for valor in matrices.values():
    for coo in valor:
        coor.append(coo)


fig,ax = plt.subplots()
figura = patches.Polygon(coor,closed=True)
#agregamos los valores la funcion
ax.add_patch(figura)

#creamos un plano cartesiano
ax.axhline(0,color = "black", linewidth = 2, )
ax.axvline(0,color = "black", linewidth = 2, )

#creamos la cudricula para mejor visualizacion 
ax.grid(True)
#creamos los limites del plano cartesiano
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

#para mostrar el plano cartesiano
plt.show()


    