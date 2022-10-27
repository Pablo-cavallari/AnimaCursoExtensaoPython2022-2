# comando input() : quero permitir que
#o usuário digite algo...
nome = input("digite seu nome: ")
idade = int( input("Digite sua idade: "))
genero = input("Digite seu gênero: M ou F ")

# comando de saída..exebir na tela
print(nome)
print(idade)

dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

if idade >= 18 and genero == "M":
  print("Você é maior de idade e precisa servir no exercito")

elif(idade >= 18 and genero == "F"):
  print("Você é maior de idade e não precisa servir no exercito")

else:
  print("Você é menor de idade e não precisa servir no exercito")
print("A Morte é inevitavel")

