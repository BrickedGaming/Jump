import pygame.freetype
import random
from pygame.locals import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
FrameRateTick = 25
clock = pygame.time.Clock()
is_started = False


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
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
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


pygame.mixer.init()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
jetsound = pygame.mixer.Sound("Assets/JetSounds.mp3")
player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True


class Menu():
    def __init__(self):
        self.surf = pygame.image.load("Assets/SplashScreen.png")
        self.rect = self.surf.get_rect(topleft=(0, 0))

        self.start_button = Button1()
        self.quit_button = Button2()

    def draw_menu(self, screen):
        screen.blit(self.surf, self.rect)


menu = Menu()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        if is_started == True:
            if event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)

            if pygame.sprite.spritecollideany(player, enemies):
                player.kill()
                pygame.quit()
                jetsound.stop()
                running = False

    screen.fill((135, 206, 250))

    if is_started == True:
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        screen.blit(player.surf, player.rect)

        pressed_keys = pygame.key.get_pressed()

        enemies.update()
        clouds.update()

        player.update(pressed_keys)


    elif is_started == False:
        menu.draw_menu(screen)

        if menu.start_button.draw(screen):
            is_started = True
        if menu.quit_button.draw(screen):
            running = False

    pygame.display.flip()
    clock.tick(FrameRateTick)
