import numpy as np
import pygame.surfarray as surfarray
import pygame
import sys
import scipy.linalg
import decimal
import random
import scipy as scipy
from pygame.locals import *
import pickle

pygame.init()

DS = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
GREEN = (25, 123, 48)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ballX = 15
slope = 0.3
intercept = 1
count = 0
trainingset = np.array([])
d = 1
d2 = 1
r1 = 0
r2 = 0
DS.fill(BLACK)
pygame.draw.rect(DS, WHITE, (0, 10, 15, 100))
# pygame.draw.rect(DS, RED, (485, 10, 15, 100))
pygame.draw.circle(DS, WHITE,
                   (ballX, int(slope*ballX + intercept)), 10, 1)
pygame.key.set_repeat(50, 50)

trainX = []
trainY = []
X = []
Y = []
while True:
    direction = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 1
                r1 -= 20
            if event.key == pygame.K_DOWN:
                direction = 0
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
            slope = float(decimal.Decimal(random.randrange(25, 200))/100)
        else:
            slope = -1*float(decimal.Decimal(random.randrange(25, 200))
                             / 100)
        slope = -slope
        intercept = current_y - slope*ballX
    if ballX < 15:
        if r1 > slope*ballX + intercept or r1 + 100 < slope*ballX + intercept:
            print("Lost")
            X = []
            Y = []
            output = 0
            ballX = 15
            slope = 0.3
            d = 1
            intercept = 1
            DS.fill(BLACK)
            pygame.draw.rect(DS, WHITE, (0, r1, 15, 100))
        #     pygame.draw.rect(DS, RED, (485, r2, 15, 100))
            pygame.draw.circle(DS, WHITE,
                               (ballX, int(slope*ballX + intercept)), 10)
            pygame.display.update()
            pass
        else:
            print("Hit")
            trainX += X
            trainY += Y
            #print(X)
            X = []
            Y = []
            current_y = slope*ballX + intercept
            intercept += 2*slope*ballX
            d = 1
            if slope > 0:
                slope = float(decimal.Decimal(random.randrange(25, 200))/100)
            else:
                slope = -1*float(decimal.Decimal(random.randrange(25, 200))
                                 / 100)
            slope = -slope
            intercept = current_y - slope*ballX
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
    X1 = surfarray.pixels2d(pygame.display.get_surface())
    
    # iska dekh le.. y ka and final trainingset ka jo bhi h
    clock.tick(100)
    DS.fill(BLACK)
    count += 1
    if(count > 500):
        with open('trainX.pkl', 'wb') as f:
            pickle.dump(trainX, f)
        with open('trainY.pkl', 'wb') as f:
            pickle.dump(trainY, f)
        pygame.quit()
        sys.exit()
    pygame.draw.rect(DS, WHITE, (0, r1, 15, 100))
    # pygame.draw.rect(DS, RED, (485, r2, 15, 100))
    pygame.draw.circle(DS, WHITE,
                       (ballX, int(slope*ballX + intercept)), 10)
    pygame.display.update()
    X += [X1.flatten()]
    Y += [direction]
    


