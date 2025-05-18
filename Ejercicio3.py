# Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

#Se realiza una variable para pedir el numero y agregarlo al diccionario
Num= int (input("Introduce un numero: "))
#Se  crea el diccionario
Diccionario = {i:i**2 for i in range(1, Num + 1)}
#Se muestra el resultado
print("Diccionario de cuadros: ")
print(Diccionario)
