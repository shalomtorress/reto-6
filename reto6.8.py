# Archivo: main.py

import reto6_7

numeros = [float(input("Ingrese el número 1: ")),
              float(input("Ingrese el número 2: ")),
              float(input("Ingrese el número 3: ")),
              float(input("Ingrese el número 4: ")),
              float(input("Ingrese el número 5: "))]

print("El promedio es:", reto6_7.promedio(numeros))
print("La mediana es:", reto6_7.mediana(numeros))
print("El promedio multiplicativo es:", reto6_7.promedio_multiplicativo(numeros))
print("Los números ordenados de forma ascendente son:", reto6_7.ordenar_ascendente(numeros))
print("Los números ordenados de forma descendente son:", reto6_7.ordenar_descendente(numeros))
print("La potencia del mayor número elevado al menor número es:", reto6_7.potencia_mayor_menor(numeros))
print("La raíz cúbica del menor número es:", reto6_7.raiz_cubica_menor(numeros))
