def calcularVelocidadeMedia(distancia, tempo):
    velocidade_media = distancia/tempo
    print("Avelocidade média é {}. Km/h".format(velocidade_media))

dist = float(input("Informe a distância "))
temp = float(input("Informe o tempo "))

calcularVelocidadeMedia(dist, temp)