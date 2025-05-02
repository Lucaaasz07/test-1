#Ejercicio 2

import random

rango_inferior=int(input("Escoga el numero limite inferior del rango"))
rango_superior=int(input("Escoga el numero limite superior del rango"))
if rango_inferior > rango_superior:
    print("El rango inferior no debe ser mayor")
else:

    numero_random=random.randint(rango_inferior,rango_superior)
    print(numero_random)

    numerofinalizado= round(numero_random/4)*4
    print(numerofinalizado)

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
             