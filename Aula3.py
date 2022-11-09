fruta1 = "morango"
fruta2 = "maça"
fruta3 = "abacaxi"

#Lista
frutas = ["morango", "maça", "abacaxi"]

#mostra todas
print(frutas)
#quero exibir apenas a 3ª. fruta (abacaxi)
print(frutas[2])

#Inclui nova fruta
frutas.append("pera")

#quantas frutas tem na lista?
print(len(frutas)) # length = tamanho


i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das futas com FOR")
for fruta in frutas:
  print(fruta)