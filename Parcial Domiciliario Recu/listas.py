from validaciones import *
from informacion import info

def mostrar_dato_lista(lista:list, indice:int, tipo:list):
    for i in range(len(tipo)):
        print(f"{tipo[i]}: {lista[indice][i]}")
        

def mostrar_lista(lista:list, tipo:list):
    for i in range(len(lista)):
        mostrar_dato_lista(lista, i, tipo)
        print("")

def buscar_dato(lista:list, dato, indice:int = -1)->int:
    encontrado = -1
    if indice == -1:
        for i in range(len(lista)):
            if lista[i] == dato:
                encontrado = i
    else:
        for i in range(len(lista)):
            if lista[i][indice] == dato:
                encontrado = i
        
    return encontrado    

def filtrar_lista(lista:list, indice:int, filtro:str)->list:
    filtrada = []
    for i in range(len(lista)):
        if lista[i][indice] == filtro:
            filtrada.append(lista[i])

    return filtrada

def encontrar_min(lista:list,indice:int)->int:
    min = lista[0][indice]
    min_indice = 0
    for i in range(1, len(lista)):
        if lista[i][indice] < min:
            min = lista[i][indice]
            min_indice = i
    
    return min_indice

def encontrar_max(lista:list,indice:int)->int:
    max = lista[0][indice]
    max_indice = 0
    for i in range(1, len(lista)):
        if lista[i][indice] > max:
            max = lista[i][indice]
            max_indice = i
    
    return max_indice

def transladar_lista(receptor:list, emisor:list):
    for i in range(len(emisor)):
        receptor.append(emisor[i])


def ordenar_alfabeticamente(lista:list, indice:int):
    ordenada = []
    for i in range(len(lista)):
        max_indice = encontrar_max(lista, indice)
        ordenada.append(lista[max_indice])
        lista.pop(max_indice)
    
    transladar_lista(lista, ordenada)
    
def crear_lista():
    lista = [
        validar_string("Ingrese nombre"),
        validar_string("Ingresar tipo"),
        validar_mayor(0, "ingrese altura"),
        validar_mayor(0, "ingrese peso"),
        validar_mayor(0, "ingrese nivel"),
        validar_mayor(0, "Ingrese fuerza de ataque"),
        validar_datos("ingrese region", ["Johto","Kanto","Sinnoh","Hoenn"]),
    ]

    return lista

