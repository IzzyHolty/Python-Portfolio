import random
import sys
import os
import pygame
pygame.init()


window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("The Pumpkin King")

character_x = 50
character_y = 420
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= velocity
    if keys[pygame.K_RIGHT]:
        character_x += velocity
    if keys[pygame.K_UP]:
        character_y-= velocity
    if keys[pygame.K_DOWN]:
        character_y += velocity

    window.fill((0,0,1))
    pygame.draw.circle(window, (pygame.Color('#e58124')), (character_x, character_y), 50, 50)
    pygame.display.update()

pygame.quit()
