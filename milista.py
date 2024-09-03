misnovias=["Ana","Anastacia","Maria"]
misnumero=[666,77,10]
#Mostrando mis novias
print(misnovias)
#mostrando msi numeros
print(misnumero)
print("--accediendo a los elementos de la lista--")
print(misnovias[2])
if "Anaa" in misnovias:
    print("si, ana esta en la lista de mis novias")
else:
    print("chale no es mi novia")
print("Numero de novias")
Nnovias=len(misnovias)
print(F"Numero de novias = {Nnovias}")
print("-------ciclo for en listas--------")
posicion=0
for medianaranja in misnovias:
    print(posicion,"",medianaranja)
    posicion=posicion+1


