#EJERCICIO 1
#Defino la variable edad como entero, para que el usuario ingrese su edad
edad = int(input("Ingrese su edad: "))
#Condicional: variable "edad" mayor o igual a 18 para determinar que es mayor de edad
if edad >= 18:
    print("Es mayor de edad")

#EJERCICIO 2
#Defino la variable nota como entero, para que el usuario ignrese su calificacion
nota = int(input("Ingrese su calificacion: "))
#Condicional: nota mayor o igual a 6 para que determine que el usuario esta aprobado, si es menor a ese valor estara desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#EJERCICIO 3
#Defino la variable numero_par como entero, para que el usuario ingrese un numero
numero_par = int(input("Ingrese numero: "))
#Condicional: numero_par que sea divisible por 2 y que el resto sea 0 para que muestre por pantalla que es par, si no es impar
if numero_par % 2 == 0:
    print("Ha ingreseado un numero par")
else: 
    print("Por favor, ingrese un numero par")

#EJERCICIO 4
#Defino edad como entereo para que el usuario ingrese la misma
edad = int(input("Ingresar edad: "))
#Condicional: segun la variable edad y su valor determinara a que categoria pertenece
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    edad >= 30
    print("Adulto/a")

    #EJERCICIO 5
#Defino contrasenia, para que el usuario ingrese la misma
contrasenia = input("Ingrese contraseña: ")
#Condicional: funcion len para obtener la longitud de la contrasenia y que rango de caracteres necesito
if len(contrasenia) > 8 and len(contrasenia) <= 14: 
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#EJERCICIO 6
#Importamos random para que cree una lista de numeros aleatorios
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print(numeros_aleatorios)
#Utilizamos statistics para determinar mode,median y mean y que arroje que sesgo es a traves de la variable numeros_aleatorios
from statistics import mode, median, mean
if (mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Sesgo positivo")
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)) and (median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print("Sesgo negativo")
else:
    if mode(numeros_aleatorios) == median(numeros_aleatorios) == mean(numeros_aleatorios):
        print("Sin sesgo")

#EJERCICIO 7
#variable frase para que el usuario ingrese la misma
frase = input("Ingrese frase o palabra: ")
#Condicional: utilizamos la funcion endswith para saber si la frase termina en vocal, si termina en vocal se le agrega ! si no se imprime normal
if frase.endswith("a") or frase.endswith("e") or frase.endswith("i") or frase.endswith("o") or frase.endswith("u"):
    print(frase,"!")
else: print(frase)

#EJERCICIO8
#variable nombre y numero para que el usuario ingrese dichos datos
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un numero (1, 2 o 3): "))
#Tomamos la variable nombre y le damos valor en minuscula, mayuscula y con su primera letra en mayuscula
nombre_mayuscula = nombre.upper()
nombre_minuscula = nombre.lower()
nombre_primerL = nombre.title()
#Segun el numero ingresado por el usuario determinara como estara escrito el nombre
if numero == 1:
    print(nombre_mayuscula)
elif numero == 2:
    print(nombre_minuscula)
else:
    if numero == 3:
        print(nombre_primerL)

#EJERCICIO 9
#Definimos magnitud como numero decimal para que el usuario ingrese la magnitud de un terremoto
magnitud = float(input("Ingrese magnitud del terremoto: "))
#Condicional: segun el numero en la escala determinara que nivel de peligro tiene el terremoto 
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    if magnitud >= 7:
        print("Extremo")

#EJERCICIO 10
#Definimos hemisferio y le damos valor en mayuscula. Definimos mes y dia como enteros
hemisferio = input("Ingrese su hemisferio (N/S): ")
hemisferio = hemisferio.upper()
mes = int(input("Ingrese mes del año (1-12): "))
dia = int(input("Ingrese que dia es: "))
#Condicional: si hemisferio = N determinara segun dia y mes en que estacion del año esta el usuario
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        print("Usted se encuentra en invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Usted se encuentra en primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Usted se encuentra en verano")
    else:
        if(mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
            print("Usted esta en otoño")
#Condicional: si hemisferio = S determinara segun dia y mes en que estacion del año esta el usuario
else:
    hemisferio == "S"
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        print("Usted se encuentra en verano")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Usted se encuentra en otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Usted se encuentra en invierno")
    else:
        if(mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
            print("Usted esta en primavera")