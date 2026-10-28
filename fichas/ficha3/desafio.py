Quantidade = 0
soma = 0
while True:
    valor = int(input("Digite um número (0 para parar): "))
    Quantidade += 1
    soma += valor
    if valor == 0:
        break
print("Quantidade de inputs:", Quantidade-1)
print("Soma dos inputs:", soma )
