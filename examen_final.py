productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}


def stock_marca(marca):
    
    total = 0
    for modulo in productos:
        if marca == productos[modulo][0].lower():
            total += stock[modulo][1]
    print("El stock es: ", total)






def busqueda_precio(p_min, p_max):
    disponibles=[]
    for modulo in stock:
        precio, stockers = stock[modulo]
        if p_min < precio < p_max and stockers > 0:
            marca = productos[modulo][0]
            disponibles.append(f"{marca}---{modulo}")
    if disponibles:
         print("Los notebooks entre los precios consultas son: ",disponibles)
    else:
         print("No hay notebooks dentro de ese rango de precios")


def actualizar_precio(modelo, p):
    
    if modelo in stock:
         stock[modelo][0]= p
    print("Precio actualizado!!")

         
       
    




    






while True:
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")


    opcion = input("Ingresar opción: ")
    if opcion =="1":
        marca = input("Ingrese marca a consultar: ").lower()
        stock_marca(marca)

    elif opcion == "2":
            try:
                p_min=int(input("Ingrese el precio mínimo: "))
                p_max=int(input("Ingrese el precio máximo: "))

                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar valores enteros!!")
            
            

            



    elif opcion == "3":
        while True:

            modelo = input("Ingrese modelo a actualizar: ")
            p = int(input("Ingrese precio nuevo: "))
            actualizar_precio(modelo, p)
    
            s = input("Desea actualizar otro precio (s/n)? ")
            if s != "si":
                    break

    elif opcion == "4":
        print("Programa Finalizado.")
        break

    else:
        print("Debe ingresar una opcion válida")
