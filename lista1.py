    # Exercício 1

numero = int(input("Digite um número inteiro: "))
resto = numero % 2
if resto == 0:
    print("Seu número é par")
else:
    print("Seu número é ímpar")

    # Exercício 2

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
if (a > b):
    print(f"{a} é maior que {b}")
else:
    print(f"{b} é maior que {a}")

    # Exercício 3

vogal = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ').lower()
if (letra in vogal):
    print(f"a letra {letra} é uma vogal")
else:
    print(f"a letra {letra} é uma consoante")
    
    # Exercício 4

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if (media == 10):
    print("Aprovado com distinção")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")

    # Exercício 5

i1 = int(input("Digite o primeiro número inteiro: "))
i2 = int(input("Digite o segundo número inteiro: "))
i3 = int(input("Digite o terceiro número inteiro: "))
m = max(i1, i2, i3)
print(f"{m} é o maior valor")

    # Exercício 6
while True:
    turno = input("Digite o turno que você estuda: \n M - Matutino \n V - Vespertino \n N - Noturno \n").lower()
    if turno == ("m"): 
        print("Bom dia!")
        break
    elif turno == ("v"):
        print("Boa tarde!")
        break
    elif turno == ("n"):
        print("Boa noite!")
        break
    else:
        print("Valor inválido")
        continue

    # Exercício 7

soma = 0
sus = input("Responda com sim ou não\nTelefonou para a vítima? ").upper()
if (sus == "SIM"):
    soma += 1
sus = input("Esteve no local do crime? ").upper()
if (sus == "SIM"):
    soma += 1
sus = input("Mora perto da vítima? ").upper()
if (sus == "SIM"):
    soma += 1
sus = input("Devia para a vítima? ").upper()
if (sus == "SIM"):
    soma += 1
sus = input("Já trabalhou com a vítima? ").upper()
if (sus == "SIM"):
    soma += 1
if (soma == 5):
    print("Você é o(a) assassino(a)")
elif (soma == 3) or (soma == 4):
    print("Você é cúmplice")
elif (soma == 2):
    print("Você é suspeito(a)")
else: 
    print("Você é inocente")

    # Fim :D