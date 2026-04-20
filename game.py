import tkinter as tk
import random

#parameters
WIDTH = 600
HEIGHT = 400

root = tk.Tk()
root.title("Dodge Arena")

canvas = tk.Canvas(root, width=WIDTH, height = HEIGHT, bg="black")
canvas.pack()

lives = 3
speed = 15
player = []
enemies = []
orbs = []
game_over = False
score = 0
sprite_data = [
    "00011000",
    "00111100",
    "01011010",
    "11011011",
    "11111111",
    "00100100",
    "01000010",
    "00100100"
]
lives_text = canvas.create_text(
        WIDTH - 80,
        20,
        text ="Lives: 3",
        fill ="white",
        font=("Arial", 14)
  )

score_text = canvas.create_text(
    80,
    20,
    text="Score: 0",
    fill="white",
    font=("Arial", 14)
)

difficulty_text = canvas.create_text(WIDTH//2, 20, text="Level: 1", fill="white", font=("Arial", 14))

def create_sprite(data, color="cyan"):
    img = tk.PhotoImage(width=16, height=16)
    for y, row in enumerate(data):
        for x, bits in enumerate(row):
            if bits == "1":
                img.put(color, (x*2, y*2, x*2+2, y*2+2))
    return img

give_sprite = create_sprite(sprite_data)

def create_player():
    global player
    player = canvas.create_image(WIDTH//2, HEIGHT//2, image=give_sprite)

def spawn_enemy():
    x = random.randint(0, WIDTH)
    enemy = canvas.create_rectangle(x, 0, x+20, 20, fill="red")
    enemies.append(enemy)

def spawn_orb():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    orb = canvas.create_oval(x, y, x+15, y+15, fill="yellow")
    orbs.append(orb)

def difficulty_scale():
    return score//200 + speed // 5

def move_enemies():
    difficulty = difficulty_scale()

    for enemy in enemies[:]:
        canvas.move(enemy, 0, 3)
        x1, y1, x2, y2 = canvas.bbox(enemy)
        if y1 > HEIGHT:
            canvas.delete(enemy)
            enemies.remove(enemy)

def collision(a, l):
    ax1, ay1, ax2, ay2 = canvas.bbox(a) 
    lx1, ly1, lx2, ly2 = canvas.bbox(l)

    return ax1 < lx2 and ax2 > lx1 and ay1 < ly2 and ay2 > ly1

def power_up():
    global speed
    if speed < 30:
        speed += 3

    print("Speed Boost!")

def reset(event=None):
    global enemies, orbs, score, game_over, lives, speed
    global lives_text, difficulty_text, score_text
    canvas.delete("all")
    enemies=[]
    orbs=[]
    score = 0
    lives = 3
    speed = 15
    game_over=False

    create_player()
    global lives_text, score_text
    lives_text = canvas.create_text(WIDTH - 80, 20, text="Lives: 3", fill="white", font=("Arial", 14))
    score_text = canvas.create_text(80, 20, text="Score: 0", fill="white", font=("Arial", 14))
    difficulty_text = canvas.create_text(WIDTH//2, 20, text="Level: 1", fill="white", font=("Arial", 14))

    game_loop()

create_player()

root.bind("r", reset)

#boundaries
def boundaries():
    x1, y1, x2, y2 = canvas.bbox(player)
    if x1 < 0 or x2 > WIDTH or y1 < 0 or y2 > HEIGHT:
        return False
    return True

def move_left(event):
    canvas.move(player, -speed, 0)
    if not boundaries():
        canvas.move(player, speed, 0)
def move_right(event):
    canvas.move(player, speed, 0)
    if not boundaries():
        canvas.move(player, -speed, 0)
def move_up(event):
    canvas.move(player, 0, -speed)
    if not boundaries():
        canvas.move(player, 0, speed)
def move_down(event):
    canvas.move(player, 0, speed)
    if not boundaries():
        canvas.move(player, 0, -speed)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

root.bind("a", move_left)
root.bind("d", move_right)
root.bind("w", move_up)
root.bind("s", move_down)

def game_loop():
    global score, game_over, lives, speed

    if game_over:
        return
    
    difficulty = difficulty_scale()
    spawn_chance = max(10, 40 - difficulty*3)
    if random.randint(1, spawn_chance) == 1:
        spawn_enemy()

    if random.randint(1, 250) == 1:
        spawn_orb()

    move_enemies()
    
   
    canvas.itemconfig(difficulty_text, text="Level: " + str(difficulty_scale()-2))

    score+=1
    canvas.itemconfig(score_text, text="Score: " + str(score))

    for enemy in enemies[:]:
        if collision(player, enemy):

            lives -=1
            canvas.itemconfig(lives_text, text="Lives: " + str(lives))

            canvas.delete(enemy)
            enemies.remove(enemy)

            if lives <= 0:
                game_over = True
                canvas.create_text(WIDTH//2, 
                HEIGHT//2, 
                text="GAME OVER", 
                fill="red", 
                font=("Arial",24)  
                )
                return   

    for orb in orbs[:]:
        if collision(player, orb):
            canvas.delete(orb)
            orbs.remove(orb)
            power_up()

    root.after(20, game_loop)
        
spawn_orb()
spawn_enemy()
game_loop()

        
root.mainloop()
