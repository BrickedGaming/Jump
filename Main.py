from Class import *
from settings import *
from menu import *

pygame.mixer.init()

pygame.init()

running = True

player = Player()

menu = Menu()

death = Death()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
jetsound = pygame.mixer.Sound("Assets/JetSounds.mp3")

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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
                is_dead = True
                jetsound.stop()

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

    if is_dead == True:
        death.draw_death(screen)

        if death.restart_button.draw(screen):
            is_started = True
            is_dead = False
        if death.quit_to_menu_button.draw(screen):
            is_started = False
            is_dead = False

    pygame.display.flip()
    clock.tick(FrameRateTick)
