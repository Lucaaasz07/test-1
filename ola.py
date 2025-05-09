#Ejercicio 1




quintil=int(input("ingrese su quintil(1, 2, 3, 4 o 5): "))
condicionacademica= float(input("Ingrese su promedio: "))
arancel=1800000
matricula=90000

if (quintil ==  1 or 2)  and condicionacademica > 6.0: 
     descuentoarancel= arancel * 0.20
     descuentoarancel2= arancel - descuentoarancel
elif (quintil == 3 or 4) and condicionacademica > 6.0:
     descuentoarancel= arancel * 0.15
     descuentoarancel2= arancel - descuentoarancel
elif (quintil ==  1 or 2) and 5.0 < condicionacademica <= 6.0:
     descuentoarancel= arancel * 0.13
     descuentoarancel2= arancel - descuentoarancel
elif (quintil ==  3 or 4)  and 5.0 < condicionacademica <= 6.0:
     descuentoarancel= arancel * 0.10
     descuentoarancel2= arancel - descuentoarancel

if (quintil == 1 or 2 or 3) and condicionacademica >= 5.5:
     matriculafinal= matricula * 0.15
     matriculafinal2 = matricula - matriculafinal
elif (quintil == 1 or 2 or 3) and condicionacademica < 5.5:
     matriculafinal= matricula * 0.15
     matriculafinal2 = matricula - matriculafinal
    
     
print(f"El valor del arancel es: {descuentoarancel2}")
print(f"El valor de la matrícula es: {matriculafinal2}")