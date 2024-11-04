########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################
import turtle

class Forma:
    def desenhar(self):
        turtle.circle(50)  

class Circulo(Forma):
    def desenhar(self):
        turtle.clear()
        turtle.penup()
        turtle.goto(0, -50)  
        turtle.pendown()
        turtle.circle(50)    

class Quadrado(Forma):
    def desenhar(self):
        turtle.clear()
        turtle.penup()
        turtle.goto(-50, 50)  
        turtle.pendown()
        for _ in range(4):    
            turtle.forward(100)
            turtle.right(90)
        
quadrado = Quadrado()
quadrado.desenhar()

circulo = Circulo()
circulo.desenhar()

turtle.done()
