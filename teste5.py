#5) Escreva um programa que inverta os caracteres de um string.

a = "DIGITE AQUI O QUE VOCÊ DESEJAR"
b = ""
dividir = []

for i in range(len(a)):
    dividir.append(a[i])

dividir.reverse()

for i in range(len(dividir)):
    b += dividir[i]

print(b)
    