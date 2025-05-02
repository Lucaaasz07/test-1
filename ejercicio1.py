#Ejercicio 1
quintil=int(input("Seleccione su quintil(1,5)"))
laboral=(input("Seleccione su condicion laboral(Empleado o Desempleado)"))
edad=int(input("Seleccione su edad"))

subsidio_base=0
bonos=0

if quintil == 1:
    subsidio_base = 15000 
    bono=+ 2000
    if laboral == "Empleado":
        subsidio_base = 0
    
elif quintil == 2:
    subsidio_base = 10000
    bono=+ 2000
    if laboral == "Desempleado":
        subsidio_base= 0
    
    bono=+ 2000
elif quintil == 3:
    subsidio_base = 8000 
    if laboral == "Empleado":
        subsidio_base = 0
elif quintil == 4:
    subsidio_base = 6000
    if laboral == "Desempleado":
        subsidio_base = 0
elif quintil == 5:
    subsidio_base = 1500

if edad > 65:
 bonoedad= 3000

total = subsidio_base + bono + bonoedad
print("Su total de subsidio es de: $", (total))