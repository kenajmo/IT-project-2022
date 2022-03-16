import pygame
import os
import character
import cream_puff

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Some const. values for later use
FPS = 60
CHARACTER_WIDTH, CHARACTER_HEIGHT = 50, 100
CHARACTER_VELOCITY = 3
START_POSITION = [0, 0]
# Some colors
GREY = (105, 105, 105)
LIME = (50, 205, 50)

# Loading the character image and the cream puff image
CHARACTER_IMAGE = pygame.image.load(os.path.join('img', 'rectangle.png'))
CREAM_PUFF_IMAGE = pygame.image.load(os.path.join('img', 'cream_puff.png'))

# creating a character and cream puff objects
character = character.Character(
  START_POSITION[0], START_POSITION[1], WINDOW, CHARACTER_IMAGE, CHARACTER_WIDTH,
  CHARACTER_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, CHARACTER_VELOCITY)

cream_puff = cream_puff.CreamPuff(450, 250, WINDOW, CREAM_PUFF_IMAGE, character)


def draw():
  WINDOW.fill(GREY)
  character.draw_character()
  cream_puff.check_collisions()
  cream_puff.draw_cream_puff()
  pygame.display.update()


def main():
  clock = pygame.time.Clock()
  run = True

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    character.move_character()

    draw()
  pygame.quit()


if __name__ == '__main__':
  main()
