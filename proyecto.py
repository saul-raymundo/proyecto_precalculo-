"""
debemos crear un proyecto de python que nos ayude a calcular el area total de una figura en el plano cartesiano, donde las 
coordenadas nos los dara el usuario, debemos calcular el area total de las cuatro secciones de un plano cartesiano, 
y debemos mostrar la figura que se llega a crear en el plano cartesiano.
"""
import matplotlib.pyplot as plt #para llamar la funcion subgraficos y para mostrar los resultados
import matplotlib.patches as patches #se encarga de llamar a la funcion POLYGON que nos graficara las coordenadas
from shapely.geometry import Polygon
from matplotlib.ticker import MultipleLocator #para poder indicar como mostrar los valores del plano cartesiano
import math


#creamos la pantalla de bienvenida al usuario 
i= 0
arrib = ("*".ljust(50,"*"))#son los marcos de arriba
print(arrib)
while True:
    forma = ("*"+ " " * 49 + "*")#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
    print(forma)
    i +=1
    if i == 2:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
        text = "BIENVENIDO".center(47)
        print("*",text,"*")
        print(forma+'\n'+ forma+"\n"+arrib)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
        break

#pedir datos al usuario y el programa se encarga de agregarlos a un dicionario de listas
matrices = {"A":[],"B":[],"C":[],"D":[]}
for name,lista in matrices.items():
    #con el ciclo while el usuario puede ingresar las cordenadas que desee.
    while True:
        dato = input(f"\n ingrese coordenadas de matriz {name}: ")
        
        if dato == "":
            break #cuando el usuario deje un espacio en blanco pasa a la siguiente matriz.
        valores = dato.split(",")
        tupae =(int(valores[0]),int(valores[1]))
        lista.append(tupae)
        print(f"\nValor ingresados de {name}: ",lista)
        print("\nPrecione ENTER para pasar a la siguiente matriz")

valoress2 = []
#itereamos sobre el diccionario para agregar las coordenadas a una lista
for valor in matrices.values():
    for coorden in valor:
        valoress2.append(coorden)#una lista con las coordenadas que ingreso el usuario
"""
ahora vamos a ordenar las coordenadas para graficar de la manera en la que nosotros lo hacemos 
para que el programa no nos traze en bruto y hayan intersecciones innecesarias y no sea complicado sacar la formula
"""
# 1. Promedio para hallar el centro (cx, cy)
cx = sum(p[0] for p in valoress2) / len(valoress2)
cy = sum(p[1] for p in valoress2) / len(valoress2)

# 2 y 3. Ordenar calculando el ángulo de cada punto (p) respecto al centro (cx, cy)
puntos_ordenados = sorted(valoress2, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

#preparamos todo para trazar de acuerdo a las cooordenadas
fig,ax = plt.subplots()

for vall in puntos_ordenados:
    plt.plot(vall[0],vall[1],marker = "o")#marcar cada uno de los puntos del plano cartesiano de acuerdo a las coordenadas

figgg = patches.Polygon(puntos_ordenados,closed=True)#se encarga de crear la figura que se forma al trazar
ax.add_patch(figgg)#se agrega al metodo para que este sea leido y presentado en pantalla


#____________________________________________________________________________________________________________
"""ahora debemos calcular el area total de esta grafica que nosotros trazamos
"""
grafica = Polygon(puntos_ordenados)
Area =grafica.area
print(f"\nEl area total de la figura es de: {Area}M²")
#_________________________________________________________________________________________________

"""hacemos unos ajustes a la visualizacion del grafico donde se trazo las coordenadas
para que parezca mas a un plano cartesiano. """

#ponemos la linea divisora de el centro del plano cartesiano 
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


    