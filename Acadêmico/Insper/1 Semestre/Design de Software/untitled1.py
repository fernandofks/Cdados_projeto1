import math

def volume(Raio):
    return 4*(math.pi*Raio**3)/3

print("O volume é {0}".format(volume(5)))

def distancia(inicio, velocidade, tempo):
    return inicio+velocidade*tempo

print("A distacia final é {0}".format(distancia(1,1,1)))

S1="Ins"
S2="per"
S=S1+S2
print(S)