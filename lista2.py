    # Exercício 1 
loop = 0
while (loop <= 100):
    print(f"{loop}")
    loop += 1

    # Exercício 2

loop = 0
n = int(input("Digite um valor inteiro: "))
while (loop <= n):
    print(f"{loop}")
    loop += 1

    # Exercício 3 

while True:
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    soma = numero1 + numero2
    print(f"{numero1} + {numero2} = {soma} ")
    pergunta = input("Deseja realizar mais uma soma? [S ou N] \nResposta: ").upper()
    if (pergunta == "S"):
        print("\n")
        continue
    elif (pergunta == "N"):
        print("Programa encerrado")
        break
        
    # Exercício 1 (Lista de Desafios)

soma = 1
sequencia = 0
while (sequencia < 500):
    print(f"{sequencia}")
    sequencia, soma = soma, sequencia + soma
print(f"{sequencia}")

    # Exercício 2 (Lista de Desafios)

perguntas = int(input("Digite quantos valores você quer: "))
valor = 1
valores = []

while (valor <= perguntas):
    numero = float(input(f"Digite o valor {valor}: " ))
    valores.append(numero)
    valor += 1

menor = min(valores)
maior = max(valores)
soma = sum(valores)

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")
print(f"A soma dos valores é {soma}")

    # Exercício 3 (Lista de Desafios)

while True:
    perguntas = int(input("Digite quantos valores você quer (valores entre 0 e 1000): \n"))
    valor = 1
    valores = []
    if (perguntas > 1000):
        print("Digite um valor menor\n")
        continue
    elif (perguntas < 0):
        print("Digite um valor maior\n")
        continue
    else:
        break

        # É a mesma coisa do exercício 2, só coloca a condição de if e else entre 1000 e 0 dentro de um loop (while True)
        
while (valor <= perguntas):
    numero = float(input(f"Digite o valor {valor}: " ))
    valores.append(numero)
    valor += 1

menor = min(valores)
maior = max(valores)
soma = sum(valores)

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")
print(f"A soma dos valores é {soma}")

    # Exercício 4 (Lista de Desafios)

p = 0 # Para no fim do código, pôr um fim no "while"
while (p == 0):
    nome = input("Digite um nome de no mínimo 4 caracteres: \n")
    if (len(nome) < 4):
        print("Nome inválido\n")
        continue
    p += 1

while (p == 1):
    idade = int(input("Digite sua idade: \n"))
    if (idade > 150) or (idade < 0):
        print("Idade inválida\n")
        continue
    p += 1

while (p == 2):
    salario = float(input("Digite seu salário: \n"))
    if (salario < 0):
        print("Salário inválido\n")
        continue
    p += 1

while (p == 3):
    sexo = input("Digite seu sexo (M ou F): \n").lower()
    if (sexo != "m") and (sexo != "f"):
        print("Sexo inválido\n")
        continue
    p += 1

while (p == 4):
    estadocivil = input("Digite seu estado civil (S, C, V ou D)\n").lower()
    if (estadocivil != "s") and (estadocivil != "c") and (estadocivil != "v") and (estadocivil != "d"):
        print("Estado civil inválido\n")
        continue
    p += 1 # Parar a condição de LOOP de "while (p == 0)"

    # Exercício 5 (Lista de Desafios)

numeroprimo = int(input("Digite um valor: "))
if numeroprimo < 2:
    print(f"{numeroprimo} não é um número primo")
else:
    divisão = 2
    while divisão < numeroprimo:
        if numeroprimo % divisão == 0:
            print(f"{numeroprimo} não é um número primo")
            break  # Encontrar divisor
        divisão += 1
    else:
        print(f"{numeroprimo} é um número primo")

        # Fim² :D