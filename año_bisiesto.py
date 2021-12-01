import sys

a = int(input("Ingrese el año: "))

if a % 400 == 0:
	print("ES BISIESTO")
elif a % 4 == 0 and a % 100 != 0:
	print("ES BISIESTO")
else:
	print("NO ES BISIESTO")
	sys.exit()
	
