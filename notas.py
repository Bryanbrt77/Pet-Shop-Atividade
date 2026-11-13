nome = input("Qual nome do aluno: ")
nota_1 = float(input("Qual a média do 1º bimestre:"))
nota_2 = float(input("Qual a média do 2º bimestre:"))
nota_3 = float(input("Qual a média do 3º bimestre:"))
nota_4 = float(input("Qual a média do 4º bimestre:"))

media = nota_1 + nota_2 + nota_3 + nota_4 / 4

print(f"Olá, {nome}! Sua média é: {media} pontos")