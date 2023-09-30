#if, elif, else, if anidados

edad = 19
cumpliste_hoy = True

if edad == 18:
    print("mayor de edad")
    if cumpliste_hoy == True:
        print("felicidades los cumpliste hoy")
    
elif edad > 18:
    print("tambien puedes pasar")
else:
    print("no puedes pasar eres menor de edad")