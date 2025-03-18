Ava1 = float(input("Qual a nota da sua primeira avaliação? "))
Ava2 = float(input("Qual a nota da sua segunda avaliação? "))
Ava3 = float(input("Qual a nota da sua terceira avaliação? "))
Ava4 = float(input("Qual a nota da sua quarta avaliação? "))

soma_das_notas_do_aluno = Ava1 + Ava2 + Ava3 + Ava4 
media_geral = soma_das_notas_do_aluno/4
print("Sua média estudantil é: ", media_geral)

if media_geral < 7: 
  print("Sua nota esta abaixo da média e você precisa realizarar a recuperação.")
elif media_geral == 7:
  print("Sua nota está na média!")
else:
  print("Parabéns, você foi aprovado e está acima da média!")
