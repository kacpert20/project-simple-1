# to jest komentarz
import pgzrun
from random import randint, choice
bounces = 0
class Paletka:

    def __init__(self, paletka, pozycja):
        self.paletka = paletka
        self.paletka.x = pozycja[0]
        self.paletka.y = pozycja[1]
    def drawing(self):
        self.paletka.draw()

    def move(self, direction):
        if direction == "left":
            self.paletka.x -= 7
        elif direction == "right":
            self.paletka.x += 7

    def bounce(self):
        global bounces
        # taki prosty zabieg nie wystarczy
        if self.paletka.distance_to(ball) > 80:
            return False
        if abs(self.paletka.y - ball.y) > 20:
            return False
        bounces += 1
        return True

def aktualizuj_pozycje_paletek():
    if paletka_a.AI == False:
        if keyboard.a:
            paletka_a.move("left")
        if keyboard.s:
            paletka_a.move("right")

    else:
        if (ball.x > paletka_a.paletka.x):
            paletka_a.paletka.x += 5
        if (ball.x < paletka_a.paletka.x):
            paletka_a.paletka.x -= 5

    if keyboard.k:
        paletka_b.move("left")
    if keyboard.l:
        paletka_b.move("right")

def update_ball_position():
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    if ball.y < 5:
        ball.winner = "GRACZ B"
        ball.stop = True
        ball.game_run = False
    elif ball.y > HEIGHT - 5:
        ball.winner = "GRACZ A"
        ball.stop = True
        ball.game_run = False

def sprawdz_czy_odbijemy():
    if paletka_a.bounce():
        ball.direction_y = "down"
    if paletka_b.bounce():
        ball.direction_y = "up"



WIDTH = 1280
HEIGHT = 853

paletka_a = Paletka(Actor("palette.png"), ((WIDTH/2),20))
paletka_b = Paletka(Actor("palette.png"), ((WIDTH/2),833))

ball = Actor("ball.png")
ball.x = randint(40, WIDTH - 40)
ball.y = HEIGHT // 2

ball.start = False
ball.game_run = False
ball.stop = False
ball.winner = None
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 4
paletka_a.AI = False

def draw():

    screen.blit("desert.jpg",(0,0))
    if not ball.start:
        screen.draw.text(
            "Naciśnij SPACJĘ aby rozpocząć. Wciśnij P, aby grać z komputerem.", (40, 150), fontsize=40, color=(0, 0, 0)
        )
    paletka_a.drawing()
    paletka_b.drawing()
    ball.draw()

def update():
    global bounces
    if keyboard.p:
        paletka_a.AI = True
    if ball.game_run == False:
        if not ball.start and keyboard.space:
            ball.game_run = True
            ball.start = True
    if ball.game_run:
        update_ball_position()
        aktualizuj_pozycje_paletek()
        sprawdz_czy_odbijemy()
    if bounces == 7:
        ball.speed += 1
        bounces += 1
    elif bounces == 15:
        ball.speed += 1
        bounces += 1
    elif bounces == 20:
        ball.speed += 1
        bounces += 1


pgzrun.go()
