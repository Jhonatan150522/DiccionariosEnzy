# Realizar un algoritmo el cual pregunte el nombre de la persona y la edad, tener en cuenta que al
# momento de mostrar la edad en pantalla debe mostrar la fecha de nacimiento de dicha persona.

#Se importa datetime 
from datetime import datetime

#Se obtiene el año actual
AñoActu = datetime.now().year

#Se le pide el nombre al usuario y edad 
Nombre = input("Introduce el Nombre: ")
Edad = int(input("Introduce la edad: "))

#Se realiza el calculo del año de nacimineto 
AñoNacim = AñoActu - Edad

#Se muestra el resultado
print(f"Hola {Nombre}, Tienes {Edad} años. ")
print(f"Naciste en el año {AñoNacim}.")