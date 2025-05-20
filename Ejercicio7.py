# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se
# almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor
# el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura,
# pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de
# factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el
# número de factura y se eliminará del diccionario. Después de cada operación el programa debe
# mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


#Se crea el diccionario
facturas= {}

#Se crea un contador 
CantidaCobro = 0

#Se realiza un blucle while para realizar el menu
while True:
    #Se le pregunta al usuario
    print("\n¿Qué deseas hacer?")
    print("1 - Añadir una nueva factura")
    print("2 - Pagar una factura existente")
    print("3 - Terminar")
    opcion = input("Introduce una opción (1, 2 o 3): ")

    if opcion == "1":
        # Añadir nueva factura
        num_factura = input("Introduce el número de factura: ")
        coste_str = input("Introduce el coste de la factura: ")
        try:
            coste = float(coste_str)  # Convertir coste a número decimal
            if num_factura in facturas:
                print("La factura ya existe. Se actualizará el coste.")
            facturas[num_factura] = coste
            print(f"Factura {num_factura} añadida con coste {coste:.2f}")
        except ValueError:
            print("Error: el coste debe ser un número válido.")
    elif opcion == "2":
        #pagar factura existente
        num_factura = input("Introduce el numero de la factura a pagar: ")
        if num_factura in facturas:
            coste = facturas.pop(num_factura) #Eliminamos la factura y guardamos  su coste 
            cantidadCobra += coste #Se suma el coste a la cantida cobrada 
            print(f"Factura {num_factura} pagada, coste{coste}")
        else:
            print("Factura no encontrada")
    elif opcion == "3":
        #Se termina el programa
        print("Programa Finalizado")
        break
    else:
        print("Opcion invalda. Intenta de Nuevo")

#Se muestra el resumen despues de cada operacio 
cantidadPendiente = sum(facturas.values()) #Se suman todas las facturas pendientes
print(f"\nCantidad cobrada hasta el momento: {cantidadCobra}")
print(f"Cantidad pendiente de cobro: {cantidadPendiente}")




