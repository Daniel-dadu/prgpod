import csv
import statistics

#promedio y moda de "age " y "bmi"

archivo = open("insurance.csv")
listaBMI = []
listaAGE = []
contador = 0
elementosBMI = 0
elementosAGE = 0
for row in csv.DictReader(archivo):
    listaAGE.append(row['age'])
    listaBMI.append(row['bmi'])
    elementosBMI += float(listaBMI[contador])
    elementosAGE += float(listaAGE[contador])
    contador += 1
#print(type(contador))
print("El promedio de bmi es igual a", round(elementosBMI/contador, 4))
print("El promedio de age es igual a", round(elementosAGE/contador, 4))

print("La moda de bmi es:", statistics.mode(listaBMI))
print("La moda de age es:", statistics.mode(listaAGE))

listaBMI.sort()
listaAGE.sort()
q1 = float(listaBMI[(contador+1)//4])
q3 = float(listaBMI[(3*contador+3)//4])
q2 = q3 - q1

print("Cuartil 1:", q1)
print("Cuartil 2:", q2)
print("Cuartil 3:", q3)