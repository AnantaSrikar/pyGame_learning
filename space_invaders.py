# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 09:34:28 2020

@author: ANANTA SRIKAR
"""

import pygame
import random
import math 

pygame.init()

score = 0

screen = pygame.display.set_mode((800,600))

#Background

background = pygame.image.load('res/background.png')

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('res/rocket.png')
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load('res/spaceship.png')

playerX = 370
playerY = 480

playerX_change = 0

def player(x, y):
    screen.blit(playerImage, (x, y)) #draws the player

# enemy

enemyImage = []

enemyX = []
enemyY = []

enemyX_change = []
enemyY_change = []

no_of_enemies = 6

for i in range (no_of_enemies):
    enemyImage.append(pygame.image.load('res/enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImage[i], (x,y))

running = True

# bullet 
bulletImage = pygame.image.load('res/bullet.png')

bulletX = 0
bulletY = 0

bulletYchange = 0
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

def isCollision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt((math.pow((bulletX - enemyX), 2) + (math.pow((bulletY - enemyY), 2))))

    if (distance < 27):
        return True
    else:
        return False

#game loop
while(running):

    screen.fill((0,0,0)) #(R, G, B)

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT): #quits game when close button is pressed
            running = False
        if (event.type == pygame.KEYDOWN):

            if (event.key == pygame.K_LEFT):
                playerX_change = -3

            if (event.key == pygame.K_RIGHT):
                playerX_change = 3
            
            if (event.key == pygame.K_SPACE):
                if (bullet_state == "ready"):
                    bulletX = playerX
                    bulletY = playerY
                    bulletYchange = -4
                    fire_bullet(bulletX, bulletY)

        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0
            
            
    #adding boundaries to player's ship       
    playerX += playerX_change

    if (bullet_state == "fire"):
        fire_bullet(bulletX, bulletY)
        bulletY += bulletYchange
    
    if (playerX < 0):
        playerX = 0
    
    elif (playerX > 736):
        playerX = 736

    for i in range(no_of_enemies):
        
        enemyX[i] += enemyX_change[i]
        
        if (enemyX[i] < 0):
            enemyX[i] = 0
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]
        
        elif (enemyX[i] > 736):
            enemyX[i] = 736
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]
        
        if (isCollision(bulletX, bulletY, enemyX[i], enemyY[i])):
            bullet_state = "ready"
            bulletY = 480
            score += 1
            print(score)
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)
        
        enemy(enemyX[i], enemyY[i], i)

    if (bulletY <= 0):
        bullet_state = "ready"
        
    player(playerX, playerY)
    
    pygame.display.update()