def validar_rango(desde:int, hasta:int, mensaje:str)->int:
    dato = int(input(f"{mensaje}({desde}-{hasta}): "))
    while dato < desde or dato > hasta:
        dato = input(f"Error. {mensaje}({desde}-{hasta}):")

    return dato

def validar_mayor(desde:int, mensaje:str):
    dato = int(input(f"{mensaje}(mayor a {desde}): "))
    while dato < desde:
        dato = input(f"Error. {mensaje}(mayor a {desde}):")

    return dato

def validar_datos(mensaje:str, opciones:list):
    valido = False
    men_opciones = ""
    for i in range(len(opciones)):
        men_opciones += f"{opciones[i]} "

    dato = input(f"{mensaje} ({men_opciones}): ")
    for i in range(len(opciones)):
        if opciones[i] == dato:
            valido = True
    
    while valido == False:
        dato = input(f"Error. {mensaje} ({men_opciones}): ")
        for i in range(len(opciones)):
            if opciones[i] == dato:
                valido = True

    return dato

def validar_string(mensaje:str):
    dato = input(f"{mensaje}: ")
    while dato == "":
         dato = input(f"Error. {mensaje}: ")

    return dato