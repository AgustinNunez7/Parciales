from informacion import *
from listas import *
from validaciones import *

continuar = True
flag_lista = False

while continuar == True:
    print(menu)
    opcion = validar_rango(1,9, "Elija una opcion")
    print("")

    if opcion == 1:
        from heroes import lista_heroes
        flag_lista = True

    elif opcion == 9:
        print("Se salio del sistema")
        continuar = False

    elif flag_lista != True:
        print("Lista no fue importada")

    else:
        match opcion:
            case 2:
                mostrar_lista(lista_heroes, info)
            case 3:
                nuevo_heroe = crear_lista()
                lista_heroes.append(nuevo_heroe)
            case 4:
                nombre = input("Ingrese nombre: ")
                eliminar_dato(lista_heroes, nombre, 0)
            case 5:
                ordenar_alfabeticamente(lista_heroes, 0)
                mostrar_lista(lista_heroes, info)
            case 6:
                alto = encontrar_max(lista_heroes, 3)
                mostrar_dato_lista(lista_heroes, alto, info)
            case 7:
                fuerte = encontrar_max(lista_heroes, 8)
                mostrar_dato_lista(lista_heroes, fuerte, info)
            case _:
                lijero = encontrar_min(lista_heroes, 4)
                mostrar_dato_lista(lista_heroes, lijero, info)