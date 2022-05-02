import pygame

pygame.mixer.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
FrameRateTick = 25
clock = pygame.time.Clock()
is_started = False

is_dead = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
