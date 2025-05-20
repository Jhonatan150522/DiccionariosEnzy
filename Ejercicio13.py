# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada
# mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada
# mes.

#Se realiza el diccionario para poder agregar 
Ahorros = {}
#Contador
TotalAhorros = 0
#Se realiza un for para repetir los meses 
for mes in range(1,12+1): #Se realiza el rango a los 12 meses
  Mes = input("Intorduzaca el mes: ")
  Ahorro = float(input("Introduzca la Cantidad de Ganancias: "))
  TotalAhorros += Ahorro

#Se agrega al diccionario
  Ahorros[Mes] = Ahorro

#Se realiza otro bucle para mostrar las rspuestas de manera Ordenad
for i in Ahorros: 
  print(f"{i} | {Ahorros[i]}")

# print(Ahorros)
print(TotalAhorros)

