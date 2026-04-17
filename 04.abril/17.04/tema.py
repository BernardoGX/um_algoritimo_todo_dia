mes = 0
while True:
    valor = input(f"Digite o valor que você gostaria de iniciar investindo:\n\n")
    
    try:
        valor_int = int(valor)
        break
    except:
        print(f"Você não digitou um número. Tente novamente\n")
        continue

while True:
    juros = input(f"De quantos por cento será os juros?\n\n")
    try:
        juros_int = int(juros)
        break
    except:
        print(f"Você não digitou um número. Tente novamente\n")
        continue

while mes <13:
    renda = valor_int * juros_int /100
    valor_int = renda + valor_int
    print(f"Mês {mes})\n Saldo total: {round(valor_int, 2)}\n")
    mes += 1


