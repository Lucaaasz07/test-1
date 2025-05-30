#Se solicita desarrollar un programa en python que permita calcular el area de varios triangulos, para esto se le solicita al usuario cuantos triangulos va a procesar
#Luego, por cada traingulo se debe ingresar la base y la altura, ambos valores positivos y reales (es decir pueden tener decimal).
#El area del triangulo se calcula con la siguiente formula, Area = (base * altura)/2
#Si su usuario ingresa un valor inválido se debe mostrar un mensaje de error




while(True):
    try:
        base= float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = (base * altura)/2
        print(f"El area del triangulo es {area}")
        break
    except ValueError:
        print("Error escoga un numero valido")
