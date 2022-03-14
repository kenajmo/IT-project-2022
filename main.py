import pygame
import os

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 60
CHARACTER_WIDTH, CHARACTER_HEIGHT = 50, 100
CHARACTER_VELOCITY = 3
GREY = (105, 105, 105)
WHITE = (50, 205, 50)

CHARACTER_IMAGE = pygame.image.load(os.path.join('img', 'rectangle.png'))


# Checks if the character can move in the given direction
def is_valid(side, char_rect):
  if side == 'left':
    if char_rect.x > 0:
      return True
    else:
      return False
  if side == 'up':
    if char_rect.y > 0:
      return True
    else:
      return False
  if side == 'down':
    if char_rect.y + CHARACTER_HEIGHT < WINDOW_HEIGHT:
      return True
    else:
      return False
  if side == 'right':
    if char_rect.x + CHARACTER_WIDTH < WINDOW_WIDTH:
      return True
    else:
      return False


def draw_character(pos_x, pos_y):
  WINDOW.blit(CHARACTER_IMAGE, (pos_x, pos_y))


def draw(char_rect):
  WINDOW.fill(GREY)
  draw_character(char_rect.x, char_rect.y)
  pygame.display.update()


def main():
  character_rect = pygame.Rect(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT)
  clock = pygame.time.Clock()
  run = True

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and is_valid('left', character_rect):  # LEFT
      character_rect.x -= CHARACTER_VELOCITY
    if keys_pressed[pygame.K_UP] and is_valid('up', character_rect):  # UP
      character_rect.y -= CHARACTER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and is_valid('down', character_rect):  # DOWN
      character_rect.y += CHARACTER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and is_valid('right', character_rect):  # RIGHT
      character_rect.x += CHARACTER_VELOCITY
    draw(character_rect)
  pygame.quit()


if __name__ == '__main__':
  main()
