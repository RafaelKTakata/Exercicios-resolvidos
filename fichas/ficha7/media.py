while True  :
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    n3 = int(input("Digite um número: "))
    if n1>20 or n2>20 or n3>20 :
        print ("digite um numero menor que 20")
        continue
    if n1<0 or n2<0 or n3<0 :
            print ("digite um numero maior que 0")
            continue

    total = (n1+n2+n3) / 3

    if total >= 9.5 :
        print (total)
        print ("passou UWU")
        parar = int(input("digite 0 para parar e outro numero qualquer para continuar: "))

    else :
        print (total)
        parar = int(input("digite 0 para parar e outro numero qualquer para continuar: "))

    if parar==0 :
        break

        
for i in range(1, 11):
    print()
