import pygame
import os
import player
import cream_puff
import enemy

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Some const. values for later use
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
PLAYER_VELOCITY = 3
PLAYER_START_POSITION = [0, 0]

ENEMY_WIDTH, ENEMY_HEIGHT = 50, 100
ENEMY_VELOCITY = 3
ENEMY_START_POSITION = [500, 0]

# Some colors
GREY = (105, 105, 105)

# Loading the player image and the cream puff image
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'rectangle.png'))
CREAM_PUFF_IMAGE = pygame.image.load(os.path.join('img', 'cream_puff.png'))
ENEMY_IMAGE = pygame.image.load(os.path.join('img', 'enemy.png'))

cream_puff = cream_puff.CreamPuff(450, 250, WINDOW, CREAM_PUFF_IMAGE, player)

player = player.Player(
    PLAYER_START_POSITION[0], PLAYER_START_POSITION[1], WINDOW, PLAYER_IMAGE, PLAYER_WIDTH,
    PLAYER_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_VELOCITY, cream_puff)

enemy = enemy.Enemy(
    ENEMY_START_POSITION[0], ENEMY_START_POSITION[1], WINDOW, ENEMY_IMAGE, ENEMY_WIDTH,
    ENEMY_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_VELOCITY, cream_puff)


def draw():
    WINDOW.fill(GREY)
    player.draw_player()
    enemy.check_collisions()
    player.check_collisions()
    cream_puff.draw_cream_puff()
    enemy.draw_enemy()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move_player()
        enemy.move_enemy()

        draw()
    pygame.quit()


if __name__ == '__main__':
    main()
