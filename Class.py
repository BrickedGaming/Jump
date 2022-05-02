import pygame.freetype
from settings import *
from pygame import *
import random


class Button1():
    def __init__(self):
        self.image = pygame.image.load("Assets/StartButton.png").convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True
                self.clicked = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        return action


class Button2():
    def __init__(self):
        self.image = pygame.image.load("Assets/QuitButton.png").convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90))
        self.clicked = False

    def draw(self, screen):

        screen.blit(self.image, self.rect)
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True
                self.clicked = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        return action


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Assets/PlayersShip.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
            jetsound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
            jetsound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
            jetsound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
            jetsound.play()
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -10)
            jetsound.play()
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 10)
            jetsound.play()
        if pressed_keys[K_a]:
            self.rect.move_ip(-10, 0)
            jetsound.play()
        if pressed_keys[K_d]:
            self.rect.move_ip(10, 0)
            jetsound.play()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Assets/bombShells.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Assets/clouds.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Death():
    def __init__(self):
        self.surf = pygame.image.load("Assets/DeathScreen.png")
        self.rect = self.surf.get_rect(topleft=(0, 0))

        self.restart_button = Button3()
        self.quit_to_menu_button = Button4()

    def draw_death(self, screen):
        screen.blit(self.surf, self.rect)


class Button3():
    def __init__(self):
        self.image = pygame.image.load("Assets/Restart.png").convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True
                self.clicked = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        return action


class Button4():
    def __init__(self):
        self.image = pygame.image.load("Assets/QuitButton.png").convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        self.clicked = False

    def draw(self, screen):

        screen.blit(self.image, self.rect)
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True
                self.clicked = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        return action


jetsound = pygame.mixer.Sound("Assets/JetSounds.mp3")
