#Actividad 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

listaMultiplosCuatro = list(range(4, 101 ,4))
print(listaMultiplosCuatro)

#Actividad 2
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. 

listaCincoElementos = ["Pepe", True, 4, "Arból", False]
print(listaCincoElementos[3]) 

#Actividad 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. 

lista_vacia = []
lista_vacia.append("Bigotes")
lista_vacia.append(6)
lista_vacia.append(False)
print(lista_vacia)

#Actividad 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Actividad 5
#El programa incializa la lista numeros con los valores 8,15,3,22,7 y luego remueve de esa lista el valor mas grande de numeros
#Luego lo imprime por pantalla

#Actividad 6
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

listaSaltosCinco = list(range(10, 31 ,5))
print(listaSaltosCinco[0])
print(listaSaltosCinco[1])

#Actividad 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "toyota"
autos[2] = "citroen"

#Actividad 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Actividad 9
# Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.

compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

#Actividad 10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

lista_anidada = [[],[],["","",""],[]]

lista_anidada[0] = 15
lista_anidada[1] = True
lista_anidada[2][0] = 25.5
lista_anidada[2][1] = 57.9
lista_anidada[2][2] = 30.6
lista_anidada[3] = False

print(lista_anidada)