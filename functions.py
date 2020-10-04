def media(nota1, nota2):
    media_aluno = (nota1 + nota2) / 2;
    return media_aluno;

primeira_nota = float(input("Informe a primeira nota: "));
segunda_nota = float(input("Informe a segunda nota: "));

print("\nA média do aluno foi: {}".format(media(primeira_nota, segunda_nota)));
