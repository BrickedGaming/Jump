import pygame
from Class import (Button1, Button2)


class Menu():
    def __init__(self):
        self.surf = pygame.image.load("Assets/SplashScreen.png")
        self.rect = self.surf.get_rect(topleft=(0, 0))

        self.start_button = Button1()
        self.quit_button = Button2()

    def draw_menu(self, screen):
        screen.blit(self.surf, self.rect)
