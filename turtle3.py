########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################
import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

t = turtle.Turtle()

def mover(ponto):
    t.goto(ponto.x, ponto.y)

# Exemplo de uso
ponto1 = Ponto(100, 100)
mover(ponto1)

turtle.done()