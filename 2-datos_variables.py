print("Datos Variables")


nombre = "Alejandro"
nombre = "Daniel"
nombre = "Caraepinga"
print(nombre)

numero = 10
numero +=5                                                    #sumar a una variable
print(numero)


bienvenida = "Hola " + nombre + " ¿cómo estás?"               #concatenar variables strigs
print(bienvenida)

bienvenida = f"Hola {numero} ¿cómo estás?"                    #concatenar f-strings 
print(bienvenida)

del nombre                                                    #borrar una variable

print("15" in bienvenida)                                     #operadores de pertenencia(in/not in)
print("15" not in bienvenida)                                 #responde True o False