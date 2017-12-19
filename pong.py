import pygame
import sys
import decimal
import random
from pygame.locals import *

pygame.init()

DS = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

GREEN = (25, 123, 48)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ballX = 15
slope = 0.3
intercept = 1
d = 1
d2 = 1
r1 = 0
r2 = 0
DS.fill(GREEN)

pygame.draw.rect(DS, BLUE, (0, 10, 15, 100))
pygame.draw.rect(DS, RED, (485, 10, 15, 100))
pygame.draw.circle(DS, (0, 255, 0),
                   (ballX, int(slope*ballX + intercept)), 10, 1)
pygame.key.set_repeat(50, 50)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                r1 -= 20
            if event.key == pygame.K_DOWN:
                r1 += 20
            if r1 <= 0:
                r1 = 0
            if r1 >= 400:
                r1 = 400
    if r2 < 0:
        d2 = 1
    if r2 > 400:
        d2 = -1
    if d2 == 1:
        r2 += 2
    if d2 == -1:
        r2 -= 2
    if ballX >= 470:
        """if r2 > slope*ballX + intercept or r2 + 100 < slope*ballX + intercept:
            print("Lost")
            ballX = 15
            slope = 0.3
            d = 1
            intercept = 1
            pygame.draw.rect(DS, BLUE, (0, r1, 15, 100))
            pygame.draw.rect(DS, RED, (485, r2, 15, 100))
            pygame.draw.circle(DS, (0, 255, 0),
                               (ballX, int(slope*ballX + intercept)), 10)
            pygame.display.update()
            pass
        else:"""
        current_y = slope*ballX + intercept
        intercept += 2*slope*ballX
        d = -1
        if slope > 0:
            slope = float(decimal.Decimal(random.randrange(0, 100))/100)
        else:
            slope = -1*float(decimal.Decimal(random.randrange(155, 389))
                             / 100)
        slope = -slope
        intercept = current_y - slope*ballX
    if ballX < 15:
        if r1 > slope*ballX + intercept or r1 + 100 < slope*ballX + intercept:
            print("Lost")
            ballX = 15
            slope = 0.3
            d = 1
            intercept = 1
            pygame.draw.rect(DS, BLUE, (0, r1, 15, 100))
            pygame.draw.rect(DS, RED, (485, r2, 15, 100))
            pygame.draw.circle(DS, (0, 255, 0),
                               (ballX, int(slope*ballX + intercept)), 10)
            pygame.display.update()
            pass
        else:
            intercept += 2*slope*ballX
            d = 1
            slope = -slope
    if slope*ballX + intercept <= 0:
        intercept += 2*slope*ballX
        slope = -slope
    if slope*ballX + intercept >= 500:
        intercept += 2*slope*ballX
        slope = -slope
    if d == -1:
        ballX -= 5
    if d == 1:
        ballX += 5
    clock.tick(100)
    DS.fill(GREEN)

    pygame.draw.rect(DS, BLUE, (0, r1, 15, 100))
    pygame.draw.rect(DS, RED, (485, r2, 15, 100))
    pygame.draw.circle(DS, (0, 255, 0),
                       (ballX, int(slope*ballX + intercept)), 10)
    pygame.display.update()
