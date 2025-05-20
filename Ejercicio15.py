# Realizar un algoritmo el cual sume los ingresos de una empresa mensualmente, teniendo en cuenta que se debe saber de qué son las ganancias y se debe pedir al usuario de cuánto dinero total se obtuvo de esa ganancia, al final se deberá saber si las ganancias son mayores a las ganancias del año pasado, entonces imprimir en pantalla que se obtuvieron más ganancias y hacer la respectiva operación para saber de cuanta diferencia fue la ganancia, si las ganancias son menores a las ganancias del año pasado imprimir en pantalla el faltante de ganancias para completar las ganancias del año pasado. GANANCIAS: Pedir al usuario que ingrese las ganancias del año pasado.

#Se realiza el diccionario
BaseBatos = {}
#Se realiza una variable con el valor del año pasado
GananciasAñoPasado= 3000000
#Tambien se realiza un contador 
Contador= 0

print("°"*80)
print("Hola usuario, porfavor digite las ganancias obtenidas")
print("°"*80)
#Se realiza un bucle para poder relizar los meses
for i in range(4):
  Meses = input(f"Porfavor Digite el Mes {i +1}: ")
  Ingreso = float(input(f"Digite las Ganancias obtenidas de {Meses}: "))
  Contador += Ingreso
  BaseBatos[Meses] = Ingreso

print("-"*100)
print("Se Mostraran los Valores y ingresos durante el año de la empresa")
print("-"*100)

# Se realiza este for para poder mostrar los meses y los ingresos mostrados
for Meses , Ingreso in BaseBatos.items():
  print (f"{Meses} | {Ingreso}")
  # print (f"La ")
# print(f" El Ingreso Total anua de la empresa es: {Contador}")
#Se muestra el valor del año pasado y el valor de año actual
print("-"*80)
print("Se realiza la comparacion entre el valor del año pasado al año actual")
print(f"Las Ganancias del año pasado son: {GananciasAñoPasado}")
print(f"Las ganancias Actuales son de: {Contador}")
print("-"*80)
#Realizo una condicional para poder comparar los ingresos del año Pasado
if Contador < GananciasAñoPasado: 
  Diferencia = Contador - GananciasAñoPasado
  print(f"Faltantes de las ganancias por {Diferencia}")
elif Contador > GananciasAñoPasado:
  Suma = Contador - GananciasAñoPasado
  print(f"Se obtuvieron mas ganacias con el valor de:{Suma} de ganancias")
elif Contador == GananciasAñoPasado:
  print("Se Obtuvieron Las mismas Ganancias del año pasado")  
else:
  print("Error")

#Se muestra el valor del año pasado y el valor de año actual
print("-"*80)
print("Se realiza la comparacion entre el valor del año pasado al año actual")
print(f"Las Ganancias del año pasado son: {GananciasAñoPasado}")
print(f"Las ganancias Actuales son de: {Contador}")




