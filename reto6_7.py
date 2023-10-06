#reto6_7.py
def promedio(numeros):

  suma = 0
  for numero in numeros:
    suma += numero
  return suma / len(numeros)


def mediana(numeros):

  numeros.sort()
  if len(numeros) % 2 == 0:
    return (numeros[len(numeros) // 2] + numeros[len(numeros) // 2 - 1]) / 2
  else:
    return numeros[len(numeros) // 2]


def promedio_multiplicativo(numeros):
  

  return (1 * numeros[0] * numeros[1] * numeros[2] * numeros[3] * numeros[4]) ** (1 / 5)


def ordenar_ascendente(numeros):

  numeros.sort()
  return numeros


def ordenar_descendente(numeros):

  numeros.sort(reverse=True)
  return numeros


def potencia_mayor_menor(numeros):

  mayor = max(numeros)
  menor = min(numeros)
  return mayor ** menor


def raiz_cubica_menor(numeros):

  menor = min(numeros)
  return menor ** (1 / 3)


if __name__ == "__main__":
  numeros = [float(input("Ingrese el número 1: ")),
              float(input("Ingrese el número 2: ")),
              float(input("Ingrese el número 3: ")),
              float(input("Ingrese el número 4: ")),
              float(input("Ingrese el número 5: "))]

  print("El promedio es:", promedio(numeros))
  print("La mediana es:", mediana(numeros))
  print("El promedio multiplicativo es:", promedio_multiplicativo(numeros))
  print("Los números ordenados de forma ascendente son:", ordenar_ascendente(numeros))
  print("Los números ordenados de forma descendente son:", ordenar_descendente(numeros))
  print("La potencia del mayor número elevado al menor número es:", potencia_mayor_menor(numeros))
  print("La raíz cúbica del menor número es:", raiz_cubica_menor(numeros))