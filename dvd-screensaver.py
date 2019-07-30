import pygame
import math
import random

pygame.init()
length = 800
height = 600
size = 1
b_length = size * 265
b_height = size * 118
win = pygame.display.set_mode((length, height))
pygame.display.set_caption('Ball Simulator')
balls = ['dvd_blue.png', 'dvd_orange.png', 'dvd_red.png', 'dvd_yellow.png', 'dvd_green.png', 'dvd_purple.png', 'dvd_light-blue.png']
ballr = random.choice(balls)
ball = pygame.image.load(ballr)
ball = pygame.transform.scale(ball, (int(b_length), int(b_height)))
x = random.randrange(0, length - b_length)
y = random.randrange(0, height - b_height)
ballr = random.choice(balls)
rot = 45
vel = 0.5
x_reflect = 1
y_reflect = 1
bounced = False
corner_hits = 0

def move(dir, offset):
    global bounced, corner_hits
    global x, y, x_reflect, y_reflect

    if y > height - b_height and y_reflect == 1:
        y_reflect = -1
        bounced = True
    elif y > height - b_height and y_reflect == -1:
        y_reflect = 1
        bounced = True

    if y < 0 and y_reflect == 1:
        y_reflect = -1
        bounced = True
    elif y < 0 and y_reflect == -1:
        y_reflect = 1
        bounced = True

    if x > length - b_length and x_reflect == 1:
        x_reflect = -1
        bounced = True
    elif x > length - b_length and x_reflect == -1:
        x_reflect = 1
        bounced = True

    if x < 0 and x_reflect == 1:
        x_reflect = -1
        bounced = True
    elif x < 0 and x_reflect == -1:
        x_reflect = 1
        bounced = True

    if bounced:
        if (x <= 0 or x >= length - b_length) and (y <= 0 or y >= height - b_height):
            print("corner hit!")
            corner_hits += 1

    rads = math.radians(dir)
    x += math.sin(rads) * offset * x_reflect
    y += math.cos(rads) * offset * y_reflect

run = True

while run:
    ballr = random.choice(balls)
    pygame.time.delay(-60)
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    move(rot, vel)
    if bounced:
        bounced = False
        ball = pygame.image.load(ballr)
        ball = pygame.transform.scale(ball, (int(b_length), int(b_height)))
        win.blit(ball, (x, y))
    else:
        win.blit(ball, (x, y))
    pygame.display.update()
