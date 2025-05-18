# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes
# se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro
# diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde
# preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al
# usuario por una opción del siguiente menú:
# ✓ Añadir cliente,
# ✓ Eliminar cliente,
# ✓ Mostrar cliente,
# ✓ Listar todos los clientes,
# ✓ Listar clientes preferentes,
# ✓ Terminar.


# Diccionario principal para guardar los clientes:
# Clave = NIF, valor = otro diccionario con datos del cliente
clientes = {}

# Bucle principal para mostrar el menú y realizar operaciones
while True:
    print("\nMenú:")
    print("1 - Añadir cliente")
    print("2 - Eliminar cliente")
    print("3 - Mostrar cliente")
    print("4 - Listar todos los clientes")
    print("5 - Listar clientes preferentes")
    print("6 - Terminar")
    
    # Pedimos al usuario que elija una opción
    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":
        # Añadir un nuevo cliente
        nif = input("Introduce el NIF: ")
        
        # Comprobamos si el NIF ya existe para evitar duplicados
        if nif in clientes:
            print("Ese NIF ya existe.")
        else:
            # Pedimos los datos del cliente
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            
            # Preguntamos si es cliente preferente y lo convertimos a True/False
            pref = input("¿Cliente preferente? (sí/no): ").lower()
            clientes[nif] = {
                "nombre": nombre,
                "dirección": direccion,
                "teléfono": telefono,
                "correo": correo,
                "preferente": pref == "sí" or pref == "si"
            }
            print("Cliente añadido.")

    elif opcion == "2":
        # Eliminar un cliente por NIF
        nif = input("Introduce el NIF a eliminar: ")
        
        # Comprobamos si el cliente existe para eliminarlo
        if nif in clientes:
            del clientes[nif]
            print("Cliente eliminado.")
        else:
            print("No existe ese cliente.")

    elif opcion == "3":
        # Mostrar datos de un cliente específico
        nif = input("Introduce el NIF a mostrar: ")
        
        if nif in clientes:
            c = clientes[nif]
            # Imprimimos los datos del cliente
            print(f"NIF: {nif}")
            print(f"Nombre: {c['nombre']}")
            print(f"Dirección: {c['dirección']}")
            print(f"Teléfono: {c['teléfono']}")
            print(f"Correo: {c['correo']}")
            print(f"Preferente: {'Sí' if c['preferente'] else 'No'}")
        else:
            print("No existe ese cliente.")

    elif opcion == "4":
        # Listar todos los clientes
        if clientes:
            print("Clientes:")
            for nif, c in clientes.items():
                print(f"- {nif}: {c['nombre']}")
        else:
            print("No hay clientes.")

    elif opcion == "5":
        # Listar solo los clientes preferentes
        pref_clients = [c for c in clientes.values() if c['preferente']]
        if pref_clients:
            print("Clientes preferentes:")
            for c in pref_clients:
                print(f"- {c['nombre']}")
        else:
            print("No hay clientes preferentes.")

    elif opcion == "6":
        # Terminar el programa
        print("Saliendo...")
        break

    else:
        # Opción inválida
        print("Opción no válida.")
