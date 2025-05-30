#EL usuario debe ingresar la temperatura en un rango entre -50° y 50°, dado eque el usuaario puede ingresar cualquier dato (incluso cadna de texto), 

#se puede usar manejo de excepciones para evitar que el programa se detenga,

#1. Si el dato ingresado no es numero entero el programa debe mostrar el sig mensaje:

 # "Error: debe ingresar un numero entero valido"

#2. Si el usuario ingresa un numero entero fuera del rango, informarmarle al usuario.

 # "Temperatura fuera del rango permitido (temperatura entre -50° y 50°)

#3. Si el usuario ingresa la temperatura correctamente:

 # "Temperatura ingresada correctamente"

#4. Debe existir una opcion para salir del programa

#5. Cuando salga del programa mostrar el mensaje:

#  "Saliendo del programa, hasta luego"  






rango_min = -50
rango_max = 50

while True:
    try:
        escogido = int(input("Escoja una temperatura entre -50° y 50°: "))
    except ValueError:
        print("Error: debe ingresar un número entero válido.")
        continue  

    if escogido < rango_min or escogido > rango_max:
        print("Temperatura fuera del rango permitido (temperatura entre -50° y 50°).")
        continue

    print("Temperatura ingresada correctamente.")

    res = input("¿Desea salir del programa? (sí o no): ")
    if res == "si" or res == "sí":
        print("Saliendo del programa, hasta luego.")
        break





