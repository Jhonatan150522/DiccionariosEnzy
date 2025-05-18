# Crear un programa en Python donde se le pregunte al usuario su nombre su edad y su número de
# documento, todo esto deberá estar almacenado en un diccionario.

#Se realiza el diccionario
Usuario ={}

#Se le piden los datos al usuario
Usuario["Nombre"] = input("Introduce tu nombre: ")
Usuario["Edad"] = input("Introduce tu edad: ")
Usuario["Documento"] = input("Introduce tu documento")
#Se Muestra el diccionario completo
print("Datos del usuario Guardados en el diccionario: ")
print(Usuario)