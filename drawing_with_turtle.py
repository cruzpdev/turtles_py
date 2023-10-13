from turtle import Turtle

def obter_distancia_e_rotacao():
    distancia = int(input("Distância em pixels: "))
    rotacao = input("ROTAÇÃO (d = direita, e = esquerda, n = não rotacionar): ").lower()
    if rotacao == "n":
        rotacao = None
        grau = 0
    else:
        grau = int(input(f"Quantos graus?: "))

    return distancia, rotacao, grau

def mover(t, distancia, rotacao, grau):
    if rotacao == "d":
        t.right(grau)
    elif rotacao == "e":
        t.left(grau)

    if distancia >= 0:
        t.forward(distancia)
    else:
        t.backward(abs(distancia))

def continuar_execucao():
    return input("Deseja continuar? (s para sim, qualquer outra tecla para não): ").lower() == "s"

def principal():
    t = Turtle()
    t.speed(1)

    while True:
        direcao = input("Para qual direção devemos ir?\n f = frente ou t = trás\n").lower()

        if direcao == "f" or direcao == "t":
            distancia, rotacao, grau = obter_distancia_e_rotacao()
            mover(t, distancia, rotacao, grau)
        else:
            print("Comando inválido")

        if not continuar_execucao():
            break

if __name__ == "__main__":
    principal()
