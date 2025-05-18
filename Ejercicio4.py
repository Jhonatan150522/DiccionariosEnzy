# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada
# asignatura en el formato tiene créditos, donde es cada una de las asignaturas del curso, y son sus
# créditos. Al final debe mostrar también el número total de créditos del curso.


Dic = {
    'Matematicas': 6,
    'Fisica': 4,
    'Quimica':5
}
#Se realiza un contador
TotalCre= 0
for Dic, creditos in Dic.items():
    print(f"{Dic} tiene {creditos} creditos")
    TotalCre =+ creditos
#Se muestra el resultado
print(f"El numero total de creditos del curso es: {TotalCre}")