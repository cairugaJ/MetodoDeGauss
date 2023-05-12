#João Enrique Rego Cairuga - 22110104 - Turma: 010
##################################################
#Cria matriz A vazia
A = []

#Solicita o tamanho da matriz
ordem = int(input("Por favor, insira o tamanho da matriz: "))

#Adiciona valores na matriz A ordemXordem
for l in range(ordem):
  linha = input("Por favor, insira os valores da linha separados por ',' : ")
  A.append(list(map(float, linha.split(','))))

#Adiciona valores no vetor b ordemX1
b = list(map(float,input("Por favor, insira os valores do vetor separados por ',' : ").split(',')))

#Expandindo a matriz A
for i in range(ordem):
  A[i].append(b[i])

print("Matriz Expandida: ")
for i in range(len(A)):
  print(A[i])

#Etapa 1: Triangularização da matriz expandida
linhas = len(A)
colunas = len(A) + 1
for i in range(ordem): #Percorre diagonal da matriz até o elemento ordemxordem
  linha_pivo = max(range(i, linhas), key=lambda j: abs(A[j][i]))
  if i != linha: #Troca linhas caso exista um pivo com valor absoluto maior na mesma coluna em outra linha abaixo, evitando divisão por 0
    A[i], A[linha_pivo] =  A[linha_pivo], A[i]
  pivo = A[i][i]
  if pivo != 0:
    A[i] = [elem / pivo for elem in A[i]] #Divide toda a linha do pivo pelo pivo para torná-lo =1
  pivo = A[i][i] #pivo = 1
  for j in range(i+1, linhas):
    mult = A[j][i] / pivo #Determina múltiplo do pivo para zerar elemento abaixo do pivo
    for k in range(i, colunas):
        A[j][k] -= mult * A[i][k]

print("Matriz Triangular Superior: ")
for i in range(len(A)):
  print(A[i])

#Etapa 2: Retrossubstituição
vetResultado = [0] * linhas
for i in range(linhas-1, -1, -1): #Percorre da última linha até a primeira
  soma = 0
  for j in range(i+1,linhas): #Percorre elementos à direita do elemento iXi
    soma += A[i][j] * vetResultado[j]
  vetResultado[i] = (A[i][-1] - soma) / A[i][i] #Adiciona valor da variável ao vetor de resposta

print("Solução: ")
print(','.join(list(map(str,vetResultado))))