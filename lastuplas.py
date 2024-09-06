arcoiris=("Azul","Verde","Rojo","Amarillo")
## muestro los elentos de la tupla
print(arcoiris)
print("\n-----------------------------------\n")
## para saber cuantos elementoss tiene la tupla
print("--Longitud del arcoiris--")
print(len(arcoiris))
print("\n-----------------------------------\n")
## guarados elemnetos de la tupla en una variable
animales=("pantera",20,"estatura",1.70)
print(animales)
print("\n-----------------------------------\n")
print("los elementos de la tupla")
## escojo que elemento deseo extraer de la tupla para poder mostrarlo
print(animales[2])
print("\n-----------------------------------\n")
rateros=("juan","ana","pedro")
y=list(rateros)
y="polainas"
x=tuple(y)
print(x)
print("\n-----------------------------------\n")
print("Agregando elementos")
## convierto la tupla en una lista para poder agragarle un elemento 
Nanimal=("body","chetos")
y=list(Nanimal)
print(y)
## elemento de deseo agregar a ala tupla
y.append("tontolin")
## vuelvo a convertir los elementos de la lista en una tupla y los muestro
otratupla= tuple(y)
print(otratupla)
print("\n-----------------------------------\n")
print("Uso for en las tuplas")
print("\n--colores dentro de arcoiris--\n")
##agarro los elementos de arcoiris y los inserto 1x1 en elcolor para poder mostrarlos 
for elcolor in arcoiris:
    print(elcolor)
