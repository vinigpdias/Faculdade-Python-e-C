notas = []

opção = -1
while opção!=4:
    print("1 - Informar notas \n 2 - Exibir notas \n Calculo da média \n 4 - sair")
    opção = int(input("Escolha sua opção: "))
    if opção==1:
        notas.append(float(input("Digite a nota! ")))
    elif opção==2:
        for x in notas:
            print(x)
    elif opção==3:
        print(sum(notas)/len(notas))          