import typing
oracion = ["Estoy", "imprimiendo", "una", "lista", "linea", "por", "linea"]

def ejercicio_0_1():
    for i in (oracion):
        print(i)

def ejercicio_0_2():
    aux = 1
    while aux <= 30:
        aux_final = aux%5
        if aux_final == 0:
            print(aux)


        aux += 1
