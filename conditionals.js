numero_sorteado = 14;
contador = 0;
tentativas = 10;
total = 0;

while(contador == 0):
    numero_escolhido = int(input("Informa a chibata do número: "));
    if(numero_escolhido == numero_sorteado):
        print("Tu acertou, seu baitinga\n");
        contador += 1;
        total = 11 - tentativas;
        print("Você utilizou {} tentativas, seu arrombado".format(total));
    else:
        print("Tu errou, seu arrombado\n");
        tentativas -= 1;
        print("Você tem {} tentativas, seu corno\n".format(tentativas));
    if(tentativas == 0):
        print("Game Over, seu leproso");
        contador += 1;
