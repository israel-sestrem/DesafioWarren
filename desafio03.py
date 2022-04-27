# Declaração de variáveis
numeros = []
resultados = []
listaTemporaria = []
total = 0
flag = True

# Valida erro do input da variável numero
while(flag):
    try:
        numero = int(input("Informe um número: "))
        flag = False
    except:
        print("Erro. Informe um valor inteiro")
flag = True

for i in range(3):
    # Valida erro do input do novo elemento da lista numeros
    while(flag):
        try:
            numeros.append(int(input("Informe o número " + str(i+1) + ": ")))
            flag = False
        except:
            print("Erro. Informe um valor inteiro")
    flag = True

# Verifica se se ir somando cada elemento da lista resulta no número informado pelo usuário
for i in range(3):
    total = 0
    listaTemporaria = []
    for j in range(numero):
        total += numeros[i]
        listaTemporaria.append(numeros[i])
        if(total == numero):
            resultados.append(listaTemporaria)
            break

# Output
print(numero)
for i in range(len(resultados)):
    print(resultados[i])