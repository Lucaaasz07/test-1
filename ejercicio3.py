#Construya un programa en python que le permita gestionar un sistema simple de venta de entradas para un cine por medio de un menu
#Dar la bienvenida al cine
#mostrar en pantalla  cuantas entradas quedan 
#comprar una cantidad de entradas de acuerdo a los usuarios
#consultar disponibilidad dentro de la sala
#consultar salida del sistema
#mostrar mensaje de despedida

print("Bienvenido al Cine")
entradas = 50
entradas_vendidas=0

while True:
    try:
        cine=int(input("""
        (1)Mostrar cantidad de entradas:
        (2)Comprar una cantidad de entradas:
        (3)Consultar disponibilidad dentro de la sala:         
        (4)Desear Salir
        """))
    
        if cine == 1:
            disponibles= entradas - entradas_vendidas
            print(f"Quedan en total {disponibles}")
        
        if cine == 2:
            cantidad = int(input("Ingrese la cantidad de entradas que quiere comprar:"))
            disponibles= entradas - entradas_vendidas

            if cantidad == 0:
             print("Debe comprar al menos 1 entrada")
            elif cantidad > disponibles:
               print("No hay suficientes entradas, solo quedan: ", disponibles)
            else:
                entradas_vendidas += cantidad
                print("Compra realizada, has comprado: ", cantidad)
   

        if cine == 3:
          disponibles = entradas - entradas_vendidas
          if disponibles > 0:
             print("Aun quedan asientos disponibles, quedan: ", disponibles)
          else:
             print("No quedan asientos disponibles")

        if cine == 4:
            print("Gracias por usar el sistema del cine de venta de entradas, Hasta luego")
            break
        
    except ValueError:
        print("Escoga un numero:")
    
          
          
          




            
        
            