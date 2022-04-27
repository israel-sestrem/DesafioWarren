# Declaração de variáveis
total = 0

for i in range(1000):
    numeroReverso = ""
    
    # Pega o valor inverso de i e adiciona à variável numeroReverso
    for j in range(len(str(i))-1,-1,-1):
        numeroReverso += str(i)[j]
    
    # Validação dos requisitos informados no exercício
    if(str(i)[0] != "0" or numeroReverso[0] != "0"):
        if((i+int(numeroReverso)) % 2 != 0):
            if (i + int(numeroReverso) < 1000000):
                print(i)
                total += 1

# Output
print("Existem " + str(total) + " números reversíveis abaixo de 1000")