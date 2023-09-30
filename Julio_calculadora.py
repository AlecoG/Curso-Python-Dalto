import sys

#Calculadora
while True:
    numero1 = input("ingrese un numero: ")
    numero1=int(numero1)
    operacion = int(input("""Elija una operación
        1-(+)
        2-(-)
        3-(*)
        4-(/)
        """))
    numero2 = int(input("Ingrese el otro número: "))

    if operacion == 1:
        print(numero1 + numero2)  

    elif operacion == 2:
        print(numero1-numero2)

    elif operacion == 3:
        print(numero1 * numero2)
        
    elif operacion == 4:
        print(numero1/numero2)
        
    else:
        print("operacion que  a seleccionado no es válida")
        