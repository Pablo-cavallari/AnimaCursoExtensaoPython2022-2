preco = 1999.90

imposto = preco * 0.05
print(imposto)

preco2 = 100

imposto2 = preco2 * 0.05
print(imposto2)

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

preco3 = 299
print(calcular_imposto(preco3))