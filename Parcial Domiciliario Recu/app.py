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
        from pokemones import lista_pokemon
        flag_lista = True
        print("Lista importada")
    elif opcion == 9:
        print("Se salio del sistema")
        continuar = False
    elif flag_lista != True:
        print("Lista no fue importada")
    else:

        match opcion:
            case 2:
                mostrar_lista(lista_pokemon, info)
            case 3:
                nuevo_mon = crear_lista()
                lista_pokemon.append(nuevo_mon)
                print("Pokemon agregado:")
                mostrar_dato_lista(lista_pokemon, len(lista_pokemon), info)
            case 4:
                nombre = input("Ingrese nombre: ")
                eliminacion = buscar_dato(lista_pokemon, nombre, 0)
                if eliminacion != -1:
                    print("Pokemon eliminado:\n")
                    mostrar_dato_lista(lista_pokemon, eliminacion, info)
                    lista_pokemon.pop(eliminacion)
                else:
                    print("Pokemon no encontrado")
            case 5:
                ordenar_alfabeticamente(lista_pokemon, 0)
                mostrar_lista(lista_pokemon, info)
            case 6:
                lista_agua = filtrar_lista(lista_pokemon, 1, "Agua")
                pesado = encontrar_max(lista_pokemon, 3)
                mostrar_dato_lista(lista_pokemon, pesado, info)
            case 7:
                fuerte = encontrar_max(lista_pokemon, 5)
                mostrar_dato_lista(lista_pokemon, fuerte, info)
            case _:
                region = validar_datos("ingrese region", ["Johto","Kanto","Sinnoh","Hoenn"])
                lista_region = filtrar_lista(lista_pokemon, 6, region)
                mostrar_lista(lista_region, info)
