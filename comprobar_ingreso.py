edad = input("Ingrese su edad:")

print(edad.isdecimal())

while edad.isdecimal() == False:
    print("Error")
    edad = input("Ingrese su edad:")
    
edad = int(edad)


if edad >= 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")
    
