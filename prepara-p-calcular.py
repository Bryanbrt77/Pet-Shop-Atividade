nome = input("Digite o nome do pet: ")
idade_humana = int(input("Digite a idade humana do pet: "))
idade_cachorro = idade_humana * 7
banhos = int(input("Digite quantos banhos o cachorro tomou: "))
porte = input("Digite o porte do pet (Grande, Médio ou Pequeno): ")

if porte == "Grande":
    valor = 20
elif porte == "Médio":
    valor = 15
elif porte == "Pequeno":
    valor = 10
else:
    valor = 0
    print("Porte inválido!")

lucro = valor * banhos

print(f"Olá, {nome} tem {idade_cachorro} e nos ultimos 12 meses o lucro com este animal foi de R${lucro},00")

