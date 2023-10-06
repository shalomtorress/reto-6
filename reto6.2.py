#reto6.2
import math
def calcular_area_y_perimetro_circulo(r):
  
  area_circulo = math.pi * r ** 2
  perimetro_circulo = 2 * math.pi * r
  return {
      "area_circulo": area_circulo,
      "perimetro_circulo": perimetro_circulo,
  }


def calcular_area_y_perimetro_rectangulo(a, b):

  area_rectangulo = a * b
  perimetro_rectangulo = 2 * (a + b)
  return {
      "area_rectangulo": area_rectangulo,
      "perimetro_rectangulo": perimetro_rectangulo,
  }


def calcular_area_y_perimetro_cuadrado(a):
  return calcular_area_y_perimetro_rectangulo(a, a)

r = float(input("Introduce el radio del círculo: "))
resultado_circulo = calcular_area_y_perimetro_circulo(r)

print(resultado_circulo)

a = float(input("Introduce el ancho del rectángulo: "))
b = float(input("Introduce el alto del rectángulo: "))
resultado_rectangulo = calcular_area_y_perimetro_rectangulo(a, b)

print(resultado_rectangulo)

