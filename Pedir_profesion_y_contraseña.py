nombre = input("Ingrese su nombre: ")
rol = input("Ingrese su profesión: ")


if rol == "Admin" or rol == "Profesor":
    contraseña = input("Ingrese su contraseña: ")
else:
    print("Error de profesión")
    rol = input("Ingrese su profesión nuevamente: ")
    contraseña = input("Ingrese su contraseña: ")  
      
while  contraseña != "1234":
    print("Error de contraseña")
    contraseña = input("Ingrese su contraseña nuevamente: ")
    

if contraseña == "1234":
    nombre = input("Ingrese su nombre: ")
    print("Hola", nombre)
elif nombre == " ":
      print("Error de nombre")
