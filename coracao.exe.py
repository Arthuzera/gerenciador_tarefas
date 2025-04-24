import turtle
import time

# Configuração inicial
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Coração para Você ❤️")

coracao = turtle.Turtle()
coracao.speed(1)
coracao.color("red")
coracao.pensize(3)
coracao.hideturtle()

# Desenha o coração
coracao.begin_fill()
coracao.left(50)
coracao.forward(100)
coracao.circle(40, 180)
coracao.left(260)
coracao.circle(40, 180)
coracao.forward(100)
coracao.end_fill()

# Mensagem romântica
coracao.penup()
coracao.goto(0, -150)
coracao.color("white")
coracao.write("Para o amor da minha vida e meu maior presente ❤️", align="center", font=("Arial", 20, "bold"))

# Assinatura
coracao.goto(0, -180)
coracao.write("Feito por: Seu branquelo 😁", align="center", font=("Arial", 10, "italic"))

# Finaliza após 5 segundos
time.sleep(10)
turtle.bye()