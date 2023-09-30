
#listas se pueden modificar
lista = ["Alejandro", "González", "Barrera", 24, True, 1.85]
print(lista[0])

#tuplas los datos no se modifican
tupla = ("Daniel", "González","Barrera", 24,True, 1.82)
print(tupla[0])


lista[0]= "Fernando"
print(lista[0])

#tupla[3] = "hoy"
#print(tupla[3])

#conjuntos -no puedo acceder a cada dato,-lo puedo modificar,-no repite datos,-datos desorenados
conjunto = {1,2,3,4,5,5,4,3,2,1}
print(conjunto)

conjunto = {2,3,4,432,4,3,2}
print(conjunto)

#diccionario
dict = {
    'nombre' : "Alejadro",
    'apellido' : "González",
    'apellido_segundo' : "Barrera",
    'edad': 24
}
print(dict['nombre'])
print(dict['apellido'])