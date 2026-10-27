#funções
def criptografar(texto):
    novo_texto = []
    for i in texto:
        if i in caracteres_especiais:
            novo_texto.append(i)
        elif i in alfabeto_minusculo:
            if texto[texto.index(i) + 1] == ' ':
                numero_final = alfabeto_minusculo.index(i) + 1
                novo_texto.append(numero_final[::-1])
            elif alfabeto_minusculo.index(i) > 19:
                novo_texto.append(alfabeto_minusculo[alfabeto_minusculo.index(i) - 21])
            else:
                novo_texto.append(alfabeto_minusculo[alfabeto_minusculo.index(i) + 5])
        else:
            return 'Deu gap'
    texto_final = ''.join(novo_texto)
    return texto_final
def descriptografar(texto):
    novo_texto = []
    for i in texto:
        if i in caracteres_especiais:
            novo_texto.append(i)
        elif i in alfabeto_minusculo:
            if texto[texto.index(i) + 1] == ' ':
                if texto[texto.index(i) - 1] in '0123456789':
                    numero_final = texto[texto.index(i) - 1] + i
                    letra_final = numero_final[::-1]
                    novo_texto.append(alfabeto_minusculo.index(letra_final - 1))
                else:
                    novo_texto.append(alfabeto_minusculo.index(i - 1))
            elif alfabeto_minusculo.index(i) < 4:
                novo_texto.append(alfabeto_minusculo[alfabeto_minusculo.index(i) + 21])
            else:
                novo_texto.append(alfabeto_minusculo[alfabeto_minusculo.index(i) - 5])
        else:
            return 'Deu gap'
    texto_final = ''.join(novo_texto)
    return texto_final
#variaveis
caracteres_especiais = '0123456789/?°|\!@#$%¨&*()_-+=¹²³£¢¬§ªº~^`.,><;:çáéóúíàèìùòãõâêûôî'
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
while True:
    decisão = input("""
    Oque você quer fazer ?:

    1 - Criptografrar
    2 - Descriptografar
    3 - Encerrar o programa

    Sua escolha:
    """)
    if decisão == '3':
        break
    elif decisão != '1' and decisão != '2':
        print("Por favor escolha uma das opções fornecidas")
    else:
        texto = list(input('Insira seu texto:').lower())
        if decisão == '1':
            print(" ")
            print(f"Aqui está seu texto criptografado: {criptografar(texto)}")
        else:
            print(" ")
            print(f"Aqui está seu texto descriptografado: {descriptografar(texto)}")
print('Fim do programa')
