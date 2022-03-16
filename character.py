import pygame

class Character:

  # Constructor
  def __init__(self, x, y, window, character_image, character_width, character_height, window_width, window_height, character_velocity):
    self.WINDOW = window
    self.CHARACTER_IMAGE = character_image
    self.CHARACTER_WIDTH = character_width
    self.CHARACTER_HEIGHT = character_height
    self.WINDOW_WIDTH = window_width
    self.WINDOW_HEIGHT = window_height
    self.CHARACTER_VELOCITY = character_velocity
    self.character_rect = pygame.Rect(x, y, self.CHARACTER_WIDTH, self.CHARACTER_HEIGHT)

  # Method for drawing the character on the screen
  def draw_character(self):
    self.WINDOW.blit(self.CHARACTER_IMAGE, (self.character_rect.x, self.character_rect.y))

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
      if self.character_rect.y + self.CHARACTER_HEIGHT < self.WINDOW_HEIGHT:
        return True
      else:
        return False
    if side == 'right':
      if self.character_rect.x + self.CHARACTER_WIDTH < self.WINDOW_WIDTH:
        return True
      else:
        return False

  # Move the character with the arrows
  def move_character(self):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and self.is_valid('left'):  # LEFT
      self.character_rect.x -= self.CHARACTER_VELOCITY
    if keys_pressed[pygame.K_UP] and self.is_valid('up'):  # UP
      self.character_rect.y -= self.CHARACTER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and self.is_valid('down'):  # DOWN
      self.character_rect.y += self.CHARACTER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and self.is_valid('right'):  # RIGHT
      self.character_rect.x += self.CHARACTER_VELOCITY
