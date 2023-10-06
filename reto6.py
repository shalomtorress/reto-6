#reto6.1
import math
def calcular_volumenYareaS(r1, r2, h):
    volumen_esfera = (4 / 3) * math.pi * r1 ** 3
    area_superficial_esfera = 4 * math.pi * r1 ** 2
    volumen_cono = (1 / 3) * math.pi * r2 ** 2 * h
    area_superficial_cono = math.pi * r2 * (r2 + math.sqrt(r2 ** 2 + h ** 2))
    return {
      "volumen_esfera": volumen_esfera,
      "area_superficial_esfera": area_superficial_esfera,
      "volumen_cono": volumen_cono,
      "area_superficial_cono": area_superficial_cono,
  }

def datos():

  r1 = float(input("Introduce el radio de la esfera: "))
  r2 = float(input("Introduce el radio de la base del cono: "))
  h = float(input("Introduce la altura del cono: "))

  return r1, r2, h

r1, r2, h = datos()
resultado = calcular_volumenYareaS(r1, r2, h)

print(resultado)

