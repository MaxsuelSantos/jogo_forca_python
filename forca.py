import random

def apresentacao():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

    print('Escolha uma lista da sua preferência:')
    print('( 1 ) Animais')
    print('( 2 ) Frutas')
    print('( 3 ) Estados')
    print('( 4 ) Países')
    print('( 5 ) Misto')


def lista_palavras(nome_arquivo='./listas/misto.txt'):
    arquivo = open(nome_arquivo, 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # sorteio de palavra
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicio_forca(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")[0].strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    apresentacao()

    pergunta_lista = int(input('Qual lista você prefere? '))

    if (pergunta_lista == 1):
        escolha_lista = './listas/animais.txt'
    elif (pergunta_lista == 2):
        escolha_lista = './listas/frutas.txt'
    elif (pergunta_lista == 3):
        escolha_lista = './listas/estados.txt'
    elif (pergunta_lista == 4):
        escolha_lista = './listas/paises.txt'
    elif (pergunta_lista == 5):
        escolha_lista = './listas/misto.txt'

    print(f'Você escolheu a lista {escolha_lista}. Boa sorte!')

    palavra_secreta = lista_palavras(escolha_lista)
    letras_acertadas = inicio_forca(palavra_secreta) # coloca '_' para cada letra da palavra gerada

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)

if(__name__ == "__main__"):
    jogar()