while True:
    largura = float(input("Coloque a largura do retângulo: "))
    altura = float(input("Coloque a altura do retângulo: "))

    if largura <= 0 or altura <= 0:
        print("A largura e a altura têm de ser maiores do que zero. Tente de novo.")
        continue

    break

print("A área do retângulo é: " + str(largura * altura))
