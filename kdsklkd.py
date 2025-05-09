#Ejercicio 2

import random
rangoinferior=int(input("Ingrese limite inferior:"))
rangosuperior=int(input("Ingrese limite superior:"))
if rangoinferior > rangosuperior: 
    print("el rango inferior debe ser menor")
else:
    
    numero_random= random.randint(rangoinferior, rangosuperior)
    while True:
        escogido1=int(input("adivina el numero:"))
        if escogido1 == numero_random:
            print(" “Felicitaciones, pudiste adivinar")
            break
        elif escogido1 < numero_random:
            print("el numero es mayor")
        else:
            print("el numero es menor")
        escogido2= int(input("Intente de nuevo:"))
        if escogido2 == numero_random:
            print(" “Felicitaciones, pudiste adivinar")
            break
        elif escogido2 < numero_random:
            print("el numero es mayor")
            print("Te dare un pista")
            distancia1 = abs(numero_random - escogido1)
            distancia2 = abs(numero_random - escogido2)
            if distancia1  < distancia2:
                print(f"el numero {escogido1} esta mas cerca que el numero {escogido2}")
            elif distancia1  > distancia2:
                print(f"el numero {escogido2} esta mas cerca que el numero {escogido1}")

        else:
            print("el numero es menor")
            distancia1 = abs(numero_random - escogido1)
            distancia2 = abs(numero_random - escogido2)
            if distancia1  < distancia2:
                print(f"el numero {escogido1} esta mas cerca que el numero {escogido2}")
            elif distancia1  > distancia2:
                print(f"el numero {escogido2} esta mas cerca que el numero {escogido1}")
        escogido3= int(input("Ultimo intento: "))
        if escogido3 == numero_random:
            print(" “Felicitaciones, pudiste adivinar")
            break
        else:
              print(f"Perdiste el numero era: {numero_random}")
              break
                
        


        

        
        
