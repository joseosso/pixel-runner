WIDTH = 800
HEIGHT = 400

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()

# Background
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Text
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = text_font.render("Hello", False, "Black")

# Snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_starting_x_pos = 800
snail_x_pos = snail_starting_x_pos
snail_speed = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= snail_speed
    if snail_x_pos < -10: snail_x_pos = snail_starting_x_pos
    screen.blit(snail_surface, (snail_x_pos, 265))

    pygame.display.update()
    clock.tick(60)