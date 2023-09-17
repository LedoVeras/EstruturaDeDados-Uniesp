notas = []
for i in range(5):
    nota = float(input(f"nota n{i+1}º: "))
    notas.append(nota)

media = round(sum(notas) / 5 , 2)

print('o aluno foi ' + ("reprovado" if media < 7 else "aprovado") + f' com média {media:.2f}.')
