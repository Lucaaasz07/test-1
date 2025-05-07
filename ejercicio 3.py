#Desarrolla un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico. El primer valor debe ser menor que el segundo. El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.

   # Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
   # Si no acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
   # En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
    #Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."


import random

rango_inferior=int(input("Escoga el numero limite inferior del rango: "))
rango_superior=int(input("Escoga el numero limite superior del rango: "))
if rango_inferior > rango_superior:
    print("El rango inferior no debe ser mayor")
else:

    numero_random=random.randint(rango_inferior,rango_superior)
    

    numerofinalizado= round(numero_random/4)*4
    

    numero_escogido=0

    while True:
        print("Aidivina el numero tienes tres intentos")
        print("")
        numero_escogido=int(input("Cual es el numero (1)"))

        if numero_escogido == numerofinalizado:
            print("Felicitaciones, adivinaste en el primer intento")
            break
        else:
            print("El numero no es correcto")
            if numero_escogido < numerofinalizado:
                print("Una pista el numero secreto es mayor")
            else: 
                print("Una pista el numero secreto es menor")

        numero_escogido=int(input("Cual es el numero (2)"))

        if numero_escogido == numerofinalizado:
            print("Felicitaciones, adivinaste en el segundo intento")
            break
        else:
            print("El numero no es correcto")
            if numero_escogido < numerofinalizado:
                print("Una pista el numero secreto es mayor")
            else: 
                print("Una pista el numero secreto es menor")
        
        numero_escogido=int(input("Cual es el numero (3)"))

        if numero_escogido == numerofinalizado:
            print("Felicitaciones, adivinaste en el tercer intento")
            break
        else:
            print("El numero no es correcto")
            if numero_escogido != numerofinalizado:
                print("Perdiste, el número era ",(numerofinalizado))
                break