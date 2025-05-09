# Actividad 1

# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101): print (i)

# Actividad 2 
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numeroEnteroUsuario = int(input("Escriba un número entero: "))
numero = abs(numeroEnteroUsuario)  # Asegurarse de que sea positivo
cantidadDigitos = 0

if numero == 0:
    cantidadDigitos = 1
else:
    while numero > 0:
        numero //= 10  # División entera
        cantidadDigitos += 1

print("El total de dígitos es:", cantidadDigitos)

# Actividad 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

valorUsuarioUno = int(input("Escriba el valor 1: "))
valorUsuarioDos = int(input("Escriba el valor 2: "))
suma = 0

for i in range(valorUsuarioUno + 1, valorUsuarioDos): 
    suma += i

print("La suma de los valores intermedios es:", suma)

# Actividad 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numeroUsuario = int
totalAcumulado = 0

while(numeroUsuario != 0):
    numeroUsuario = int(input("Escriba numeros enteros: "))
    totalAcumulado += numeroUsuario

print("El total acumulado es: ", totalAcumulado)

# Actividad 5

# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numeroRandom = random.randint(0, 9)
numeroAdivinado = int
numeroIntentos = 0

while(numeroAdivinado != numeroRandom):
    numeroIntentos = numeroIntentos + 1
    numeroAdivinado = int(input("Escriba numeros enteros: "))

print("Adivino el número!. El numero de intentos fue: ", numeroIntentos)

#Actividad 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(101,-1,-1): 
    if(i % 2 == 0):
        print (i)

# Actividad 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

valorUsuario = int(input("Ingrese un numero positivo mayor a 0: "))
suma = 0

if(valorUsuario > 0):
    for i in range(0, valorUsuario + 1): 
        suma += i

    print("La suma de los valores intermedios es:", suma)

# Actividad 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos

limiteNumeros = 5
insercionUsuario = 1
sumaPares = 0
sumaPositivos = 0
sumaNegativos = 0
sumaImpares = 0

while(insercionUsuario != limiteNumeros + 1):
    valorUsuario = int(input(f"Ingrese el numero {insercionUsuario}: "))
    insercionUsuario += 1

    if(valorUsuario % 2 == 0):
        sumaPares += 1
        if(valorUsuario < 0):
            sumaNegativos += 1
        elif(valorUsuario > 0):
            sumaPositivos += 1
    elif(valorUsuario % 2 == 1):
        sumaImpares += 1
        if(valorUsuario < 0):
            sumaNegativos += 1
        elif(valorUsuario > 0):
            sumaPositivos += 1

print(f"Hay {sumaPares} numeros pares")
print(f"Hay {sumaImpares} numeros impares")
print(f"Hay {sumaNegativos} numeros negativos")
print(f"Hay {sumaPositivos} numeros positivos")

# Actividad 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.

limiteNumeros = 3
insercionUsuario = 1
mediaTotal = 0
sumaTotal = 0

while(insercionUsuario != limiteNumeros + 1):
    valorUsuario = int(input(f"Ingrese el número {insercionUsuario}: "))
    insercionUsuario += 1
    sumaTotal += valorUsuario

mediaTotal = sumaTotal / limiteNumeros
print(f"La media es {mediaTotal}")

# Actividad 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario

numero = input("Ingrese un número: ")
numeroInvertido = ""

for caracter in numero[::-1]:
    invertido += caracter

print("El número invertido es:", numeroInvertido)

