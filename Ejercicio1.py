# 1. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
# un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en
# <dirección> y su número de teléfono es <teléfono>.

#Se le pide al usuario los datos
print("Este Programa Recolecta sus datos")
Nombre = input("Porfavor Digite su Nombre Completo: ")
edad=int(input("Porfavor Digite la edad: "))
Direccion= input("Digite Su direccion: ")
Telefono=int(input("Digite su numero Telefonico: 0"))
print("-"*80)
#Se realiza el diccionario con las claves 
Diccionario={
'Nombre': Nombre,
'edad':edad,
'Direccion':Direccion, 
'Telefono':Telefono
}
#Se muestran los resultados
print(Diccionario['Nombre'],'Tiene', Diccionario['edad'], 'años, vive en', Diccionario['Direccion'],'y su numero telefonico es',Diccionario['Telefono'])







#Este es la expicacion de alvaro sobre el ejercicio 2
# # # Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
# # # usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
# # # de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# # Fruta= {
# #   'platano': 1.35,
# #   'Manzana': 0.80,
# #   'Pera': 0.85,
# #   'Naranja': 0.70
# # }
# # fruta= input("Ingrese la fruta: ").lower()
# # #Condicional para buscar dentro de la lista
# # if fruta in Fruta:
# #   print("Digite los kilos")
# #   kilo=int(input("Digite los kilos: "))
# # Resultado= 