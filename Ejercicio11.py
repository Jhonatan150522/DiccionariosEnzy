# 11. Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la
# información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán
# listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo
# sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista
# de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un
# alumno que ya existe el programa nos dará un error.


#Se realiza los diccionarios 
alumnos = {}

#Se pide cuantos alumnos se van a introducior
NumAlumnos = int(input("Cuantos alumnos se introducen?: "))

#Se realiza un for para repetir el proceso para cada alumno
for i in range(NumAlumnos):
    print(f"Alumno{i+1}: ")
    #Se le pide el numero al alumno
    Nombre = input("Nomnbre del alumno: ")
    #Se verifica si el alumno esta
    if Nombre in alumnos:
        print("Error: ese nombre ya fue ingresado")
        continue #Se salta al siguinte alumno 
#Se realiza una lista de las notas
Notas = []
#Se introduce un bucle que se rompe al momento de introducior un numero negativo
while True:
    nota = float(input("Introduce una nota(Numero negativo para terminar): "))
    if nota < 0: 
        break
    Notas.append(nota)#Se agrega a la lista
#Se guarda el alumno y sus notas en el diccionario
alumnos[Nombre]=Notas
#Se muestran los resultados finales
print("Notas medias de los alumnos:")
for nombre, notas in alumnos.items():
    if notas: #Se evita la divicion por cero
        media = sum(notas) / len(notas)
        print(f"- {nombre}: {media}")
    else:
        print(f"- {nombre}: No tiene notas registradas")


