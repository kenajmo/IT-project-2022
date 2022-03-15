import pygame
import os

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

# Loading the character image
CHARACTER_IMAGE = pygame.image.load(os.path.join('img', 'rectangle.png'))
CREAM_PUFF_IMAGE = pygame.image.load(os.path.join('img', 'cream_puff.png'))


# Character class
class Character:

  # Constructor
  def __init__(self, x, y):
    self.character_rect = pygame.Rect(x, y, CHARACTER_WIDTH, CHARACTER_HEIGHT)

  # Method for drawing the character on the screen
  def draw_character(self):
    WINDOW.blit(CHARACTER_IMAGE, (self.character_rect.x, self.character_rect.y))

  # Checks if the character can move in the given direction
  def is_valid(self, side):
    if side == 'left':
      if self.character_rect.x > 0:
        return True
      else:
        return False
    if side == 'up':
      if self.character_rect.y > 0:
        return True
      else:
        return False
    if side == 'down':
      if self.character_rect.y + CHARACTER_HEIGHT < WINDOW_HEIGHT:
        return True
      else:
        return False
    if side == 'right':
      if self.character_rect.x + CHARACTER_WIDTH < WINDOW_WIDTH:
        return True
      else:
        return False

  # Move the character with the arrows
  def move_character(self):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and self.is_valid('left'):  # LEFT
      self.character_rect.x -= CHARACTER_VELOCITY
    if keys_pressed[pygame.K_UP] and self.is_valid('up'):  # UP
      self.character_rect.y -= CHARACTER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and self.is_valid('down'):  # DOWN
      self.character_rect.y += CHARACTER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and self.is_valid('right'):  # RIGHT
      self.character_rect.x += CHARACTER_VELOCITY

character = Character(START_POSITION[0], START_POSITION[1])

# Cream puff class that will create a cream puff object
class CreamPuff:
  CREAM_PUFF_WIDTH = 50
  CREAM_PUFF_HEIGHT = 50
  cream_puff_rectangle = None
  visible = True

  def draw_cream_puff(self):
    if self.visible:
      WINDOW.blit(CREAM_PUFF_IMAGE, (self.cream_puff_rectangle.x, self.cream_puff_rectangle.y))

  def __init__(self, pos_x, pos_y):
    self.cream_puff_rectangle = pygame.Rect(pos_x, pos_y, self.CREAM_PUFF_WIDTH, self.CREAM_PUFF_HEIGHT)

  def check_collisions(self):
    if self.cream_puff_rectangle.colliderect(character.character_rect):
      self.visible = False


cream_puff = CreamPuff(450, 250)


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
