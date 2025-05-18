# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe
# preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.

#Se realiza el diccionario donde se nombra como cesta
cesta = {}

#Se realiza un bucle con while 
while True:
    articulo = input("Introduce un artículo (o escribe 'fin' para terminar): ").strip()
    if articulo.lower() == 'fin':
        break
    try:
        precio = float(input(f"Introduce el precio de {articulo}: "))
        cesta[articulo] = precio
    except ValueError:
        print("Precio no válido. Intenta de nuevo.")

#Se muestra la lista de la compra
print("La lista de la compra: ")
Total= 0
for articulo, precio in cesta.items():
    print(f"- {articulo}: {precio} $")
    Total =+ precio
#Se muestra el resultado final
print(f"Coste Total: {Total:2f}")