# 10. En una escuela se necesita un programa el cual gestione la cantidad de personas que entran a cuyo
# salón, teniendo en cuenta que se debe que tener la información personal de cada estudiante y de
# los profesores, así mismo, se debe tener un registro del número del salón al cual se le valla a hacer
# la gestión y que al final se muestre en pantalla.
# Pedir el número del salón
numero_salon = input("Introduce el número del salón: ")

# Lista para guardar la información de cada persona (estudiantes o profesores)
personas = []

# Bucle para ingresar varias personas
while True:
    print("\nNueva persona:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    documento = input("Número de documento: ")
    tipo = input("¿Es estudiante o profesor?: ").strip().lower()

    # Crear un diccionario con los datos de la persona
    persona = {
        "nombre": nombre,
        "edad": edad,
        "documento": documento,
        "tipo": tipo
    }

    # Agregar la persona a la lista
    personas.append(persona)

    # Preguntar si desea ingresar otra persona
    continuar = input("¿Deseas agregar otra persona? (sí/no): ").strip().lower()
    if continuar != "sí" and continuar != "si":
        break

# Mostrar todos los datos al final
print(f"\nRegistro del salón número {numero_salon}:")
print("Personas registradas:")
for i, p in enumerate(personas, start=1):
    print(f"\nPersona {i}:")
    print(f"  Tipo: {p['tipo'].capitalize()}")
    print(f"  Nombre: {p['nombre']}")
    print(f"  Edad: {p['edad']}")
    print(f"  Documento: {p['documento']}")
    