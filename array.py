nomes = [];

for i in range(0, 5):
    nomes.append(input("Insira o {} nome: ".format(i + 1)));
for i in range(0 , 5):
    print("{}° nome: {}".format(i + 1, nomes[i]));
