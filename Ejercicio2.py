# Escribir un programa que guarde en un diccionario los precios de las 
# frutas de la tabla, pregunte al usuario por una fruta, un número de kilos 
# y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta 
# no está en el diccionario debe mostrar un mensaje informando de ello.
#Se realiza el diccionario con sus respetivos valores o precios

Frutas = {
  'Platano': 1.35,
  'Manzana': 0.80,
  'Pera': 0.85,
  'Naranja': 0.70
}
opcion = str(input("Que fruta desea llevar?: "))

#Se agrega un condicional
if opcion in Frutas:
    kilos = float(input(f"Cuantos Kilos de {opcion} desea llevar? "))
    precio = kilos * Frutas[opcion]
    print(f"El precio de {opcion} es de {precio}")
else:
    print("Error de digitacion")