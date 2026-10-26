"""
debemos crear un proyecto de python que nos ayude a calcular el area total de una figura en el plano cartesiano, donde las 
coordenadas nos los dara el usuario, debemos calcular el area total de las cuatro secciones de un plano cartesiano, 
y debemos mostrar la figura que se llega a crear en el plano cartesiano.
"""
import matplotlib.pyplot as plt #para llamar la funcion subgraficos y para mostrar los resultados
import matplotlib.patches as patches #se encarga de llamar a la funcion POLYGON que nos graficara las coordenadas
from shapely.geometry import Polygon
from shapely.validation import make_valid
from matplotlib.ticker import MultipleLocator #para poder indicar como mostrar los valores del plano cartesiano
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
        tupae =(int(valores[0]),int(valores[1]))
        lista.append(tupae)
        print(f"valor ingresados de {name}: ",lista)

valoress2 = []
#itereamos sobre el diccionario para agregar las coordenadas a una lista
for valor in matrices.values():
    print(valor,"el buche")
    for coorden in valor:
        valoress2.append(coorden)

print(valoress2)
#creamos los valores para el grafico o subgrafico. 
fig,ax = plt.subplots()
#____________________________________________________________________________________________________________
grafica = Polygon(valoress2)
subgraf = make_valid(grafica)
#iterar sobre los valores validados para calcular el area:
area = 0 
for puntos in valoress2:
    plt.plot(puntos[0],puntos[1],marker = "o")
for elemnt in subgraf.geoms:
    x,y = elemnt.exterior.xy
    ax.fill(x,y,label = "hola")
    #plt.plot(x,y,marker = "o", color="black",linewidth =  0.8)
    print(f"la primera figura tiene un area de: {elemnt.area}")
    area += elemnt.area
   
print(f"el area total de la figura es de: {area}")
#_________________________________________________________________________________________________
#creamos un plano cartesiano
ax.axhline(0,color = "black", linewidth = 2, )
ax.axvline(0,color = "black", linewidth = 2, )

#creamos la cudricula para mejor visualizacion 
ax.grid(True)
#creamos los limites del plano cartesiano
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
#indicamos que el plano debe representarse en numeros enteros de 1 a 10
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

#para mostrar el plano cartesiano
plt.show()


    