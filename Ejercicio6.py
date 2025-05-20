# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las
# palabras español e inglés separadas por dos puntos, y cada par: separados por comas. El programa
# debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español
# y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario
# debe dejarla sin traducir.

# Pedimos al usuario que introduzca las palabras en formato "español:inglés" separadas por comas
entrada = input("Introduce las palabras español:inglés separadas por comas: ")

# Creamos un diccionario vacío para almacenar las traducciones
traducciones = {}

# Separamos la entrada en pares usando la coma como separador
pares = entrada.split(",")

# Recorremos cada par para separarlo en palabra en español y su traducción en inglés
for par in pares:
    # Comprobamos que el par contiene los dos puntos que separan español e inglés
    if ":" in par:
        # Separamos el par en dos partes: español e inglés
        esp, ing = par.split(":")
        # Eliminamos posibles espacios en blanco alrededor de las palabras
        esp = esp.strip()
        ing = ing.strip()
        # Guardamos en el diccionario la palabra en español como clave y su traducción en inglés como valor
        traducciones[esp] = ing

# Pedimos al usuario que introduzca una frase en español para traducir
frase = input("Introduce una frase en español para traducir: ")

# Separamos la frase en palabras individuales usando el espacio como separador
palabras = frase.split()

# Creamos una lista vacía para almacenar las palabras traducidas o las originales si no hay traducción
resultado = []

# Recorremos cada palabra de la frase
for palabra in palabras:
    # Buscamos la traducción en el diccionario; si no existe, usamos la palabra original
    traduccion = traducciones.get(palabra, palabra)
    # Añadimos la traducción o la palabra original a la lista resultado
    resultado.append(traduccion)

# Unimos las palabras traducidas en una sola cadena separadas por espacios
frase_traducida = " ".join(resultado)

# Mostramos la frase traducida al usuario
print("Frase traducida:", frase_traducida)