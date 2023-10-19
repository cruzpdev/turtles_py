from turtle import Turtle
t = Turtle()

def obter_distancia():
    distancia = int(input("Distância em pixels: "))
    return distancia

def rotacionar(turtle):
    rotacao = input("ROTAÇÃO (d = direita, e = esquerda, n = não rotacionar): ").lower()
    if rotacao == "d":
        rotacionar_direita (turtle)
    elif rotacao == "e":
        rotacionar_esquerda (turtle)

def rotacionar_direita (turtle):
    angulo = int(input("Ângulo de rotação para direita: "))
    t.right(angulo)
def rotacionar_esquerda(turtle):
    angulo = int(input("Ângulo de rotação para esquerda: "))
    t.left(angulo)

while True:
    direcao = input("DIREÇÃO (f = frente, t = trás): ").lower()
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar(t)
        t.backward(distancia)
    resposta = input("Continuar andando? (s/n): ").lower()
    if resposta not in ("s"):
        break
