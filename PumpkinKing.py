import random
import sys
import os
import pygame
pygame.init()

#Global Variables
screen_width = 500
screen_height = 500

character_x = 50
character_y = 440
width = 40
height = 60
velocity = 10
boundary = 13


def keyPress():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_x > boundary:
        character_x -= velocity
    if keys[pygame.K_RIGHT] and character_x < screen_width + boundary:
        character_x += velocity
    if keys[pygame.K_UP] and character_y > boundary:
        character_y-= velocity
    if keys[pygame.K_DOWN] and character_y < screen_height + boundary:
        character_y += velocity

def drawGame():
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Pumpkin King")

    run = True
    while run:
        pygame.time.delay(80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keypress()

        window.fill((0,0,1))
        pygame.draw.circle(window, (pygame.Color('#e58124')), (character_x, character_y), 50, 50)
        pygame.display.update()

    pygame.quit()

#Main
drawGame()