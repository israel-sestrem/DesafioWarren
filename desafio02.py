# Declaração de variáveis
tempoChegada = []
totalAlunosPontuais = 0
flag = True

# Valida erro do input da variável minimoAlunosPresentes
while(flag):
    try:
        minimoAlunosPresentes = int(input("Informe o limite de alunos presentes: "))
        flag = False
    except:
        print("Erro. Informe um valor inteiro")
flag = True

for i in range(5):
    # Valida erro do input do novo elemento da lista tempoChegada
    while(flag):
        try:
            tempoChegada.append(int(input("Informe o tempo de chegada do aluno " + str(i+1) + ": ")))
            flag = False
        except:
            print("Erro. Informe um valor inteiro")
    flag = True

# Verifica quantos foram os alunos pontuais e aplica o valor à variável totalAlunosPontuais
for i in range(len(tempoChegada)):
    if(tempoChegada[i] <= 0):
        totalAlunosPontuais += 1

# Output
if(totalAlunosPontuais >= minimoAlunosPresentes):
    print("Aula normal")
else:
    print("Aula cancelada")