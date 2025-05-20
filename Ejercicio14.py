# Conozca si tiene que declarar el impuesto de renta desde el próximo año, según sus ingresos
# mensuales, si sus ingresos mensuales son mayores de 3.000.000 se le deberá cobrar 250.000 más la
# implementación de un IVA del 18% de los ingresos mensuales, si los ingresos mensuales son
# menores a 3.000.000 se le cobrara 200.000 más la implementación del IVA aproximadamente del
# 10% de sus ingresos mensuales.

#Se realiza el diccionario para poder agregar los valores y las claves
Basedatos = {
  'A': 'se le deberá cobrar 250.000 más la implementación de un IVA del 18% de los ingresos mensuales',
  'b': 'se le cobrara 200.000 más la implementación del IVA aproximadamente del 10% de sus ingresos mensuales.'
}
#Se realiza las variables 
print("Vamos a calcular para comprobar si tiene que declar impuestos de renta el proxima")
IngMes= float(input("Digite la cantidad Mensula de sus ganacias: "))

if IngMes > 3000000: #Si el ingreso el mayor a 3.000.000
  Cobro = 3000000-250000 * 0.18 #cobrar 250.000 más la implementación de un IVA del 18%
  print (Basedatos["A"])
elif IngMes < 3000000: #si los ingresos mensuales son menores a 3.000.000
  Cobro = 3000000-200000*0.10
  print(Basedatos['b'])