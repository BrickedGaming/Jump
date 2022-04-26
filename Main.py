import sys

import pygame
from self import *
from pygame import *

pygame.init()
vec = pygame.math.Vector2

Height = 450
Width = 400
ACC = .5
Fric = -.12
FPS = 60

FramesPerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Jump")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))
        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


def move(self):
    self.acc = vec(0, 0)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        self.acc.x = -ACC
    if pressed_keys[K_RIGHT]:
        self.acc.x = ACC


self.acc.x += self.vel.x * Fric
self.vel += self.acc
self.pos += self.vel + 0.5 * self.acc

if self.pos.x > Width:
    self.pos.x = 0
if self.pos.x < 0:
    self.pos.x = Width

self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((Width, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(Width / 2, Height - 10))



PT1 = Platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        displaysurface.fill((0, 0, 0))

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        pygame.display.update()
        FramesPerSec.tick(FPS)


