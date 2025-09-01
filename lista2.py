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

        # :D²