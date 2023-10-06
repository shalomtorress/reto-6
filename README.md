# Reto 6
# punto 1 
+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*
```pyton
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
```
La función ```calcular_volumenYareaS```utiliza las fórmulas matemáticas para calcular el volumen y el área superficial de una esfera y un cono.
Para utilizar el número π en Python, se importo ```math``` luego, se puede utilizar la función ```math.pi``` para obtener el valor de π.
# punto 2
+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*


````python
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
````
La función ```calcular_area_y_perimetro_circulo()``` utiliza las fórmulas matemáticas para calcular el área y el perímetro de un círculo.
La función ```calcular_area_y_perimetro_rectangulo()``` utiliza las fórmulas matemáticas para calcular el área y el perímetro de un rectángulo.
# punto 3 
una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
````python
def calcular_carne_aves(N:float, M:float, K:float) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))
  total_carne = calcular_carne_aves(N, M, K)
  print("La cantidad de carne es:" + str(total_carne))
````
+ se calcula la cantidad de carne de cada tipo de ave.
+ Suma las tres cantidades para obtener la cantidad total de carne de aves.
La función también tiene  ```if __name__ == "__main__":```  la función pide los valores de ```N, M y K.```
# punto 4
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
````python
def calcular_vueltas(P, M, H, B):
  total_panes = P * 300
  total_leche = M * 3300
  total_huevos = H * 350
  total = total_panes + total_leche + total_huevos

  if B >= total:
    vueltas = B - total
    return vueltas
  else:
    return -(total - B)


if __name__ == "__main__":
  P = int(input("Número de panes: "))
  M = int(input("Número de bolsas de leche: "))
  H = int(input("Número de huevos: "))
  B = float(input("Valor del billete: "))

  vueltas = calcular_vueltas(P, M, H, B)

  if vueltas >= 0:
    print("Las vueltas son:", vueltas)
  else:
    print("Faltan:", vueltas)
````
+ Primero, calcula el costo total de los panes, la leche y los huevos.
+ Luego, comprueba si el valor del billete es mayor o igual que el costo total. Si es así, el programa calcula las vueltas y las devuelve. De lo contrario, el programa calcula lo que queda debiendo y lo devuelve.
# punto 5 
un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

````python
def calcular_interes(C, i, n):

  interes_mensual = i / 12
  valor_final = C * (1 + interes_mensual) ** n
  return valor_final


if __name__ == "__main__":
  C = float(input("Capital inicial: "))
  i = float(input("Tasa de interés anual: "))
  n = int(input("Número de meses: "))

  valor_final = calcular_interes(C, i, n)

  print("El valor del préstamo al final del período es:", valor_final)
````
+ Primero, calcula el interés mensual.
+ despue se usa la fórmula del interés compuesto para calcular el valor del préstamo al final del período.
+  imprime el valor del préstamo al final del período.
# punto 6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

````python
def calcular_contagios(C, D):
  contagiados = C
  for i in range(D):
    contagiados = contagiados * 2
  return contagiados


if __name__ == "__main__":
  C = int(input("Número de contagiados actuales: "))
  D = int(input("Número de días: "))

  contagiados = calcular_contagios(C, D)

  print("El número total de contagiados es:", contagiados)
````
+ la variable ```contagiados``` contiene el número de contagiados actuales.
+ se ```for``` para iterar D veces
En cada iteración se multiplica contagiados por 2, devuelve el valor de contagiados.

# punto 7
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

````python
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
````
se definen las funciones para las operaciones necesarias
+ ```promedio()```: Calcula el promedio de una lista de números reales.
+ ```mediana()```: Calcula la mediana de una lista de números reales.
+ ```promedio_multiplicativo()```: Calcula el promedio multiplicativo de una lista de números reales.
+ ```ordenar_ascendente()```: Ordena una lista de números reales de forma ascendente.
+ ```ordenar_descendente()```: Ordena una lista de números reales de forma descendente.
+ ```potencia_mayor_menor()```: Calcula la potencia del mayor número elevado al menor número.
+ ```raiz_cubica_menor()```: Calcula la raíz cúbica del menor número.
# punto 8
````python
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
````
# punto 9
Pip en python es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python y descargarlos a nuestra computadora con la finalidad de integrarlos a nuestros desarrollos realizado en python
# punto 10
+ NumPy es una biblioteca para cálculo numérico. Proporciona una estructura de datos de matriz multidimensional y funciones para realizar operaciones matemáticas y estadísticas en matrices.
```pip install numpy```
+ SciPy es una biblioteca para ciencia e ingeniería. Proporciona una amplia gama de funciones para el análisis de datos, la simulación numérica y el aprendizaje automático.
```pip install scipy```
+ Pandas es una biblioteca para análisis de datos. Proporciona estructuras de datos y herramientas para manipular y analizar datos tabulados.
```pip install pandas```
+ Matplotlib es una biblioteca para visualización de datos. Proporciona funciones para crear gráficos y diagramas.
```pip install matplotlib```
