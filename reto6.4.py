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
