fila = int(input("Ingrese el numero de fila: "))
columna = int(input("Ingrese el numero de columna: "))

matriz = [[3.3,6.1,4.0], [4.9, 5.7, 6.4]]

while type(fila) != int:
    print("Error")
    fila = float(input("Ingrese el numero de fila: "))
    fila = int(fila)
    break

while type(columna) != int:
    print("Error")
    columna = int(input("Ingrese el numero de columna: "))
    columna = int(columna)
    break


if fila < len(matriz):
    if columna < len(matriz):
        print(matriz[fila][columna])
    else:
        print("Error en la fila")
else:
    print("Error en la columna")
