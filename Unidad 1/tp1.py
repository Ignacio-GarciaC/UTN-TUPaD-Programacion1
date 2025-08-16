#EJERCICIO 1)
print("Hola mundo!")

#EJERCICIO 2)
nombre = input("Ingrese nombre: ")
print(f"Hola {nombre} !")

#EJERCICIO 3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#EJERCICIO 4)
import math

radio = float(input("Ingrese el radio: "))
area =  math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El area del circulo es {area} y su perimetro es {perimetro}")

#EJERCICIO 5)
segundos = float(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600

print(f"Los {segundos} equivalen a {horas}") 

#EJERCICIO 6)
numero = int(input ("Ingresar numero: "))
print(numero*0)
print(numero*1)
print(numero*2)
print(numero*3)
print(numero*4)
print(numero*5)
print(numero*6)
print(numero*7)
print(numero*8)
print(numero*9)
print(numero*10)

#EJERCICIO 7)
a = int(input("Ingrese numero: "))
b = int(input("Ingrese numero: "))
suma = a + b
div = a / b
mult = a * b
rest = a - b

print(f"El resultado de a + b es {suma}")
print(f"El resultado de a / b es {div}")
print(f"El resultado de a * b es {mult}")
print(f"El resultado de a - b es {rest}")

#EJERCICIO 8)
altura = int(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
metros = altura * 1 / 100
imc = peso / metros ** 2

print(f"Tu indice de masa corporal es {imc}")

#EJERCICIO 9)
celsius = float(input("Ingrese grados celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius es equivalente a {fahrenheit} Fahrenheit")

#EJERCICIO 10)
numero1 = float(input("Ingrese numero: "))
numero2 = float(input("Ingrese numero: "))
numero3 = float(input("Ingrese numero: "))

promedio = (numero1 + numero2 + numero3) /3

print(f"El promedio de los tres numeros es {promedio}")