import turtle

class LSystem:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom # инициатр
        self.state = axiom # строка с набором команд для фрактала
        self.width = width # толщина линии рисованияя
        self.length = length # длина одного лнейного сигмента кривой
        self.angle = angle # фиксированный угол поворота
        self.t = t  # черепашка
        self.rules = {} # словарь для хранения правил формирования кревых
        self.t.pensize(self.width) # ширина линии рисования

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def drow_turtle(self, start_pos, start_angle):
        turtle.tracer(1, 0) # скорость черепашки
        self.t.up() # черепашка поднимается на верх
        self.t.setpos(start_pos) # начальная стартовая позиция
        self.t.seth(start_angle) # начальный угол поворота 
        self.t.down() # черепашка опускается вниз

        for move in self.state:
            if move == "F":
                self.t.forward(self.length)
            elif move == "S": # для формирования более сложных фракталов
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == "+":
                self.t.left(self.angle)
            elif move == "-":
                self.t.right(self.angle)
        
        turtle.done() # используем что бы окно не закрывалось после отрисовки изображения 

#  прописываем что бы окно появилось, с размерами 1200х600
width = 1100
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)

t = turtle.Turtle()
t.ht() #  прописываем что бы черепашка не была видна

pen_width = 2 # толщина линни рисования 
f_len = 4 # длина одного сегмента прямой (в пикселах)
angle = 90 # фиксированный угол поворота 

# axiom = "F--F--F" # Снежинка Коха, угол должен быть 60 (angle = 60), правило(l_sys.add_rules(("F", "F+F--F+F")) и l_sys.generate_path(4))
# axiom = "F-F-F-F" # фрактал 2

axiom = "F+F+F+F" # фракиал 3

l_sys = LSystem(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F+F--F+F")) #для Снежинуи Коха
# l_sys.add_rules(("F", "F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F")) # для фрактала 2
l_sys.add_rules(("F", "F+S-FF+F+FF+FS+FF-S+FF-F-FF-FS-FFF"), ("S", "SSSSSS")) #для фрактала 3
l_sys.generate_path(2)
l_sys.drow_turtle((0, 0), 0)

