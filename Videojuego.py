from tkinter import *
import random

Game_width = 700
Game_height = 600
Speed = 60
Space_size = 50
body_part = 3
snake_color = "#00FF00"
Food_color = "#FF0000"
background_color = "#000000"


class Snake:
    def __init__(self):
        self.body_size = body_part
        self.coordinates = []
        self.squares = []

        for i in range(0, body_part):
            self.coordinates.append([0,0])

        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + Space_size, y +Space_size, fill= snake_color, tag = "snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (Game_width // Space_size ) -1) * Space_size
        y = random.randint(0, (Game_height // Space_size ) -1) * Space_size

        self.coordinates = [x,y]
        canvas.create_oval(x, y , x + Space_size, y + Space_size, fill= Food_color, tag = "food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= Space_size
    elif direction == "down":
        y += Space_size
    elif direction == "left":
        x -= Space_size
    elif direction == "right":
        x += Space_size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + Space_size, y + Space_size, fill= snake_color)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        score +=1
        label.config(text = "Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])
 
        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:

        ventana.after(Speed, next_turn, snake, food)


def change_direction(new_direction):

    global direction
    if new_direction =='left':
       if direction != 'right':
           direction = new_direction
    elif new_direction =='right':
       if direction != 'left':
           direction = new_direction
    elif new_direction =='down':
       if direction != 'up':
           direction = new_direction
    elif new_direction =='up':
       if direction != 'down':
           direction = new_direction



def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= Game_width:
        return True
    
    elif y < 0 or y >= Game_height:
        return True
    

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
        
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ('consolas', 70), text= "GAME OVER", fill= "red", tags = 'Gameover')


ventana = Tk()
ventana.title("Juego de la serpiente")
ventana.resizable(False, False)

score = 0
direction = "down"

label = Label(ventana, text = "Score: {}".format(score), font = ('consolas', 40))
label.pack()

canvas = Canvas(ventana, bg = background_color, height= Game_height, width= Game_width)
canvas.pack()

ventana.update()

ventana_width = ventana.winfo_width()
ventana_height = ventana.winfo_height()
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

x = int((screen_width/2) - (ventana_width/2))
y = int((screen_height/2) - (ventana_height/2))

ventana.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

ventana.bind('<Left>', lambda event: change_direction('left'))
ventana.bind('<Right>', lambda event: change_direction('right'))
ventana.bind('<Up>', lambda event: change_direction('up'))
ventana.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

ventana.mainloop()