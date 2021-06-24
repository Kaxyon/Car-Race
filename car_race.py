import pygame
import random
import time
pygame.init()

# Display
gameWindow = pygame.display.set_mode((800, 600))
pygame.display.update()

# Colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
light_green = (0,150,0)
blue=(0,0,255)
gray=(119,118,110)
car_img = pygame.image.load("car.jpg")
car_img=pygame.transform.scale(car_img, (100, 100))
grass_img = pygame.image.load("grass.jpg")
background_img = pygame.image.load("background.jpg")

# Game Variables
clock = pygame.time.Clock()

# Text
def Message(size, msg, x_pos, y_pos):
    font = pygame.font.SysFont(None, size, bold=True, italic=False)
    render = font.render(msg, True, blue)
    gameWindow.blit(render, (x_pos, y_pos))

Message(100, "START", 500, 300)
clock.tick(50)

# Car
def car(x, y):
    gameWindow.blit(car_img, (x, y))
    gameWindow.blit(grass_img, (0, 0))
    gameWindow.blit(grass_img, (700, 0))
    if 0<x<90 or 700<x+100:
        Message(100, "GAME OVER", 200, 200)
        pygame.display.update()
        clock.tick(1)
        game_intro()

# Enemy Car
def enenmy_car(x_r, y_r):
    gameWindow.blit(car_img, (x_r, y_r))

# Buttons
def button(x_button, y_button, msg_b):
    pygame.draw.rect(gameWindow, green, [x_button, y_button, 100, 30])
    Message(50, msg_b, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(gameWindow, light_green, [x_button, y_button, 100, 30])
        Message(50, msg_b, x_button, y_button)
        if click == (1,0,0) and msg_b == "PLAY":
            Gameloop()
        elif click == (1,0,0) and msg_b == "QUIT":
            pygame.quit()
            quit()

# Car Crash
def car_crash(x, x_r, y, y_r):
    if x_r<x<x_r+90 and y_r<y<y_r+90 or x_r<x+90<x_r+90 and y_r<y<y_r+90:
        Message(50, "CRASHED", 300, 200)
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

# Score
def score(count):
    font = pygame.font.SysFont(None, 30, bold=False, italic=False)
    screen_text = font.render("Score : " + str(count), True, white)
    gameWindow.blit(screen_text, (0,0))

# Game Intro
def game_intro():
    intro = False
    while intro == False:
        gameWindow.blit(background_img, (0, 0))
        button(100, 300, "PLAY")
        button(600, 300, "QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = True
        pygame.display.update()

# Gameloop
def Gameloop():
    count = 0
    x = 300
    y = 490
    x_r = random.randrange(100, 600)
    y_r = 0
    x_change = 0
    y_change = 0
    # Game Loop
    game_over = False
    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = +10
                elif event.key == pygame.K_RIGHT:
                    x_change = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0        

        gameWindow.fill(gray)
        car(x, y)
        score(count)
        enenmy_car(x_r, y_r)
        y_r += 10
        if y_r == 600:
            x_r = random.randrange(100, 600)
            y_r = 0
            count += 1
        car_crash(x, x_r, y, y_r)
        x = x - x_change
        clock.tick(50)
        pygame.display.update()

game_intro()
pygame.display.update()
pygame.quit()
quit()