#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

faturamento = []
diaMes = 5
valor = 0
media = 0
diaMaior = 0

for i in range(diaMes):
    faturamento.append(float(input("Digite o faturamento do dia (se for final de semana ou feriado basta digitar 0): ")))

    if faturamento[i] == 0:
        diaMes -= 1
        del(faturamento[i])
    else:
        media += faturamento[i]

menor = faturamento[0]
maior = faturamento[0]
media = media/diaMes
    
for i in range(diaMes):

    if maior < faturamento[i]:
        maior = faturamento[i]
    
    if menor > faturamento[i]:
        menor = faturamento[i]
    
    if faturamento[i] > media:
        diaMaior += 1

print('O menor valor apresentado no mês: {0} \nO maior valor apresentado no mês: {1} \nA média do mês: {2} \nO número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {3}'.format(menor, maior, media, diaMaior))

