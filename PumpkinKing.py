import random
import sys
import os
import pygame
pygame.init()

#Global Variables
screen_width = 500
screen_height = 500
character_x = 50
character_y = 450


def keyPress(x_pos, y_pos, scr_width, scr_height):
    boundary = 13
    isJump = False
    jumpCount = 10
    width = 40
    height = 60
    velocity = 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x_pos > boundary:
        x_pos -= velocity
    if keys[pygame.K_RIGHT] and x_pos < scr_width + boundary:
        x_pos += velocity
    if not (isJump):
        if keys[pygame.K_UP] and y_pos> boundary:
            y_pos-= velocity
        if keys[pygame.K_DOWN] and y_pos < scr_height + boundary:
            y_pos += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y_pos -= (jumpCount ** 2) * 0.5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

def drawGame():
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Pumpkin King")

    run = True
    while run:
        pygame.time.delay(80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keyPress(character_x, character_y, screen_width, screen_height)

        window.fill((0,0,1))
        pygame.draw.circle(window, (pygame.Color('#e58124')), (character_x, character_y), 50, 50)
        pygame.display.update()

    pygame.quit()

#Main
drawGame()