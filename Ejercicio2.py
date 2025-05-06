# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Se realiza el diccionario con sus respetivos valores o precios
Frutas = {
  'Platano': 1.35,
  'Manzana': 0.80,
  'Pera': 0.85,
  'Naranja': 0.70
}
fruta= input("Ingrese la fruta: ").lower()#Use lower para las mayusculas o minuscula
#Condicional para buscar dentro de la lista
if fruta in Frutas:
  print("Digite los kilos")
  kilo=int(input("Digite los kilos: "))
  Resultado= kilo*Frutas
print(Resultado)
