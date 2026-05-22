from validaciones import *
from informacion import info

def mostrar_dato_lista(lista:list, indice:int, tipo:list):
    for i in range(len(tipo)):
        print(f"{tipo[i]}: {lista[indice][i]}")
        

def mostrar_lista(lista:list, tipo:list):
    for i in range(len(lista)):
        mostrar_dato_lista(lista, i, tipo)
        print("")

def eliminar_dato(lista:list, dato, indice:int = -1):
    for i in range(len(lista)):
        if indice == -1:
            if lista[i] == dato:
                lista.pop(i)
                break
        else:
             if lista[i][indice] == dato:
                print("Eliminado:\n")
                mostrar_dato_lista(lista, i, info)
                lista.pop(i)
                break

def encontrar_min(lista:list,indice:int)->int:
    min = lista[0][indice]
    min_lista = lista[0]
    for i in range(1, len(lista)):
        if lista[i][indice] < min:
            min = lista[i][indice]
            min_lista = i
    
    return min_lista

def encontrar_max(lista:list,indice:int)->int:
    max = lista[0][indice]
    max_lista = lista[0]
    for i in range(1, len(lista)):
        if lista[i][indice] > max:
            max = lista[i][indice]
            max_lista = i
    
    return max_lista

def transladar_lista(receptor:list, emisor:list):
    for i in range(len(emisor)):
        receptor.append(emisor[i])


def ordenar_alfabeticamente(lista:list, indice:int):
    ordenada = []
    for i in range(len(lista)):
        min_heroe = lista[encontrar_min(lista, indice)]
        ordenada.append(min_heroe)
        eliminar_dato(lista, min_heroe)
    
    transladar_lista(lista, ordenada)
    
def crear_lista():
    lista = [
        validar_string("Ingrese nombre"),
        validar_string("Ingresar identidad"),
        validar_datos("ingrese empresa", ["DC Comics","Marvel Comkics"]),
        validar_mayor(0, "ingrese altura"),
        validar_mayor(0, "ingrese peso"),
        validar_datos("Ingrese genero", ["M", "F", "NB"]),
        validar_string("Ingrese color de ojos"),
        validar_string("ingrese color de pelo"),
        validar_mayor(0, "Ingrese fuerza"),
        validar_datos("ingrese inteligencia", ["low","average","high","good","genius"])
    ]

    return lista

