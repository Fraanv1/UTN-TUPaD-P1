#Actividad 1

# Escribir un programa que solicite la edad del usuario
edadUsuario = int(input("Escriba su edad: "))

# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
if edadUsuario >= 18:
    print("Es mayor de edad")

#Actividad 2
#Escribir un programa que solicite su nota al usuario.
notaUsuario = int(input("Escriba su nota: "))

# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”
if notaUsuario >= 6:
  print("Aprobado")
# En caso contrario deberá mostrar el mensaje “Desaprobado”.
else:
   print("Desaprobado")

#Actividad 3
# Escribir un programa que permita ingresar solo números pares
numeroUsuario = 1

while(numeroUsuario % 2 != 0):
   #En caso contrario, imprimir por pantalla "Por favor, ingrese un número par"
   numeroUsuario = int(input("Por favor, ingrese un número par: "))
   
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"
print("Ha ingresado un número par")

#Actividad 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece
edadUsuario = int(input("Escriba su edad por favor: "))

#Niño.
if edadUsuario < 12:
  print("Niño")
# Adolescente.
elif (edadUsuario >= 12 and edadUsuario < 18):
   print("Adolescente")
#Adulto/a joven
elif (edadUsuario >= 18 and edadUsuario < 30):
   print("Adulto/a joven")
#Adulto/a
else:
   print("Adulto/a")

#Actividad 5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14)
contrasenia = input("Escriba su contraseña: ")

while(len(contrasenia) < 8 or len(contrasenia) > 14):
   print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
   contrasenia = input("Escriba su contraseña: ")

print("Ha ingresado una contraseña correcta")

#Actividad 6
#Escribir un programa que tome la lista numeros_aleatorios
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Calcular la moda
modeResult = mode(numeros_aleatorios)
#Calcular la mediana
medianResult = median(numeros_aleatorios)
#Calcular la media
meanResult = mean(numeros_aleatorios)

#Se imprimen los resultados
print("Mediana: ", medianResult)
print("Moda: ", modeResult)
print("Media: ", meanResult)

#Comparacion
if(meanResult > medianResult) and (medianResult > modeResult):
   print("Sesgo positivo")
elif(meanResult < medianResult) and (medianResult < modeResult):
   print("Sesgo negativo")
else:
   print("Sin sesgo")

#Actividad 7
# Escribir un programa que solicite una frase o palabra al usuario. 

#Si el string ingresado termina con vocal, añadir un signo de exclamación
#al final e imprimir el string resultante por pantalla

fraseUsuario = input("Escriba una frase: ")
if fraseUsuario[-1].lower() in "aeiou":
    fraseUsuario += "!" 

# Imprimir el resultado
print("Su frase es: ", fraseUsuario)

#Actividad 8
nombreUsuario = input("Ingrese su nombre: ")
opcionUsuario = int(input("Ingrese una opcion: 1 , 2 o 3: "))

if (opcionUsuario == 1):
   print(nombreUsuario.upper())
elif(opcionUsuario == 2):
   print(nombreUsuario.lower())
else:
   print(nombreUsuario.title())

#Actividad 9
#Escribir un programa que pida al usuario la magnitud de un terremoto
magnitud = float(input("Ingresá la magnitud del terremoto: "))

#Clasifique la magnitud en una de las siguientes categorías según la escala de Richter
if magnitud < 3:
   print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
   print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
   print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
   print("Fuerte (puede causar daños en estructuras débil8es).")
elif 6 <= magnitud < 7:
   print("Muy Fuerte (puede causar daños significativos).")
else: 
   print("Extremo (puede causar graves daños a gran escala).")


#Actividad 10
# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").strip().upper()
mes = int(input("¿Que mes es? (1-12): "))
dia = int(input("¿Que día es? (1-31): "))

# Determinar la estación
if hemisferio == 'N':
      if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
      elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
      elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Verano"
      else:  
            estacion = "Otoño"
else:
      if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Verano"
      elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
      elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
      else: 
            estacion = "Primavera"

print("Estás en", estacion)
