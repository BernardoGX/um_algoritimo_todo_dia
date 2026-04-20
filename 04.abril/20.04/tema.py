def main():
    
    while True:
        erros = []
        senha = input("Digite uma senha forte:\n\n")

        tem_maiuscula = any(char.isupper() for char in senha)
        if tem_maiuscula == False:
            erros.append("Não possui um caractér maiusculo")

        tem_numero = any(char.isdigit() for char in senha)
        if tem_numero == False:
            erros.append("Não existem números")

        mais_de_oito_caracteres = len(senha) >8
        if mais_de_oito_caracteres == False:
            erros.append("Não possui mais de oito caracteres")

        if erros:
            mensagem_de_erro(erros)
            continue
        
        print("A sua senha foi aprovada")
        break


def mensagem_de_erro(erros):
    print(f"A sua senha não é forte pelo seguinte(s) motivo(s):\n{erros}")


main()