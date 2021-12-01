pack = input("Ingrese su paquete por favor: ")

paq_a = "Cancún 7 noches + Aéreos u$s por 1200 persona"
paq_b = "Miami 8 noches + Aéreos + Alquiler de Auto u$s 1500 por persona"
paq_c = "Bariloche 10 noches + Aéreos + Excursiones u$s 1300 por persona"
paq_d = "Rio de Janeiro 10 nohes + Aéreos + excursiones u$s 1400 por persona"

if pack == "a":
	print(paq_a)
elif pack == "b":
	print(paq_b)
elif pack == "c":
	print(paq_c)
elif pack == "d":
	print(paq_d)
else:
	print("Paquete elegido incorrecto")
