#EJERCICIO 1

numero = 0 #defino numero como 0
for numero in range(0,101,1): #lista de numeros del 1 al 100 sumando de a uno
    print(numero) #imprimo variable numero con su lista

#EJERICIO 2
numero = int(input("Ingrese un numero entero: ")) #le pido un numero al usuario

contador_de_digitos= len(str(numero)) #utilizo la funcion len para longitud de la cadena y str para convertir a cadena

print(f"El numero {numero} tiene {contador_de_digitos} digitos") #imprimo el numero y su digito

#EJERCICIO 3
num1 = int(input("Ingrese numero: ")) #numeros ingresados por el usuario
num2 = int(input("Ingrese numero: "))
suma = 0 

for i in range (num1 + 1,num2): #toma los numeros entre los dos valores dados
    suma += i #se suma el numero acumulado

print(f"La suma entre los numeros dados {num1} y {num2} es : {suma}") #suma de los numeros comprendidos

#EJERCICIO 4
CORTE = 0 #corte en el cual cuando se pone 0 se termina el bucle
suma = 0
numero = int(input("Ingrese numero: ")) #valor ingresado por usuario

while numero != CORTE: #mientras numero sea diferenta a corte se suma el numero acumulado
    suma += numero
    numero = int(input("Ingrese numero: ")) #valor ingresado por usuarip

print(f"El total de la suma es: {suma}") #total de la suma luego de CORTAR con 0

#EJERCICIO 5
import random #importamos randmo para luego utilizar la funcion de numero aleatorio

numero_aleatorio = random.randint(0,9) #rango de 0 a 9
intentos = 0 #definimos variable intentos donde se va a guardar la cantidad de los mismos

numero = int(input("Ingrese un numero: ")) #valor ingresado por usuario

while numero != numero_aleatorio: #mientras numero sea diferente a numero aleatorio
    intentos = intentos + 1 #se suma un intento
    numero = int(input("Ingrese otro numero: ")) #si no se acierta el usuario ingresa otro numero

intentos += 1 
print(f"Felicitaciones el numero era {numero_aleatorio}") #imprime el numero
print(f"Lo lograste en {intentos} intentos") #imprime cantidad de intentos

#EJERICIO 6
numero = 0
for numero in range(100,-1,-2): #rango de numeros del 0 al 100 empezando de -1 asi toma el 0 y -2 para que vaya en orden decreciente
    print(numero) #imprimimos numeros dando todos los numeros pares

#EJERCICIO 7
num = int(input("Ingrese un numero: ")) #valor ingresado por usaurio
suma = 0

for i in range(0,num + 1): #para i rango de 0 al numero dado por el usuario
    suma += i #sumamos el numero mediante el contador
print(f"La suma de los numeros entre 0 y {num} es: {suma}") #imprimimos la suma entre el 0 y el numero dado por usuario

#EJERCICIO8
num = 0
par = 0    #definimos las variables num,par,impar,negativo y positivo en 0 aqui se guardaran los valores correspondientes
impar = 0
negativo = 0
positivo = 0

contador = 0 #contador que arranca de 0
cantidad = 100 #contador que llega hasta 100
while contador < cantidad: #mientras contador sea menor a cantidad se ejecutara
    num = int(input(f"Ingresar el numero{contador+1}: ")) #ingresamos el numero y se suma uno al contador
    if num % 2 == 0: #si numero es par se suma a la variable par
        par += 1
    else: #si no es par se suma a la variable impar
        num % 2 != 0
        impar += 1
        
    if num > 0: #si es mayor a 0 entonces se suma a positivo
        positivo += 1
    elif num < 0: #si es menor a 0 se suma a negativo
        negativo += 1

    print(f"Los numeros pares son: {par}") #luego se imprimen que numeros son par, impar, negativo y positivo que cumplieron con cada una de sus condiciones
    print(f"Los numeros impares son: {impar}")
    print(f"Los numeros positivos son: {positivo}")
    print(f"Los numeros negativos son: {negativo}")

#EJERCICIO 9
suma = 0 
contador = 0 #contador desde 0
cantidad = 100 #contador hasta 100

while contador < cantidad: #mientras contador sea menor a cantidad se ejecutara
    numero = int(input(f"Ingrese un numero {contador + 1}: ")) #valor ingresado por el usuario
    suma += numero #suma el numero a variable suma
    contador += 1 #aumenta el contador

media = suma /cantidad #calculo de la media de los numeros dados
print(f"La media de los numeros ingresados es: {media}") #imprime la media de los mismos

#EJERCICIO 10
numero = int(input("Ingrese un numero: ")) #valor ingresado por usuario
invertido = 0

while numero != 0: #mientras numero sea diferente a 0
    digito = numero % 10 #547 % 10 = 7
    invertido = invertido * 10 + digito
    numero = numero // 10 #547 // 0 = 54

print(f"El numero invertido es: {invertido}") #imprimimos numero invertido