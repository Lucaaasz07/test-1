#hacer un menu que le presente las siguientes opciones de un usuario.
#Un saludo al colocar el num 1
#una despedida al presionar el num 2
#Una edad 
#Opcion invalida


repet= 0
while repet ==0:

    print("Si presionas 1 tendras un saludo o si apretas 2 tendras una despedida")


    usuario=int(input("Escribe una de las dos opciones: "))
    edad= int(input("Escribe tu edad: "))
    3


    if usuario == 1:
        print("Bienvenido")
        print ("Tienes ",edad)

    elif usuario == 2:
        print("Adios")
        print ("Tienes ",edad)

    else:
        print("Opcion invalida")

    ola = input("Desea continuar si o no")
    if ola == "si":
        repet = repet + 0
    else:
        repet = repet + 1


