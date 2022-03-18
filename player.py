import pygame

class Player:

  # Constructor
  def __init__(self, x, y, window, player_image, player_width, player_height, window_width, window_height, player_velocity):
    self.WINDOW = window
    self.PLAYER_IMAGE = player_image
    self.PLAYER_WIDTH = player_width
    self.PLAYER_HEIGHT = player_height
    self.WINDOW_WIDTH = window_width
    self.WINDOW_HEIGHT = window_height
    self.PLAYER_VELOCITY = player_velocity
    self.player_rect = pygame.Rect(x, y, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)

  # Method for drawing the player on the screen
  def draw_player(self):
    self.WINDOW.blit(self.PLAYER_IMAGE, (self.player_rect.x, self.player_rect.y))

  # Checks if the player can move in the given direction
  def is_valid(self, side):
    if side == 'left':
      if self.player_rect.x > 0:
        return True
      else:
        return False
    if side == 'up':
      if self.player_rect.y > 0:
        return True
      else:
        return False
    if side == 'down':
      if self.player_rect.y + self.PLAYER_HEIGHT < self.WINDOW_HEIGHT:
        return True
      else:
        return False
    if side == 'right':
      if self.player_rect.x + self.PLAYER_WIDTH < self.WINDOW_WIDTH:
        return True
      else:
        return False

  # Move the player with the arrows
  def move_player(self):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and self.is_valid('left'):  # LEFT
      self.player_rect.x -= self.PLAYER_VELOCITY
    if keys_pressed[pygame.K_UP] and self.is_valid('up'):  # UP
      self.player_rect.y -= self.PLAYER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and self.is_valid('down'):  # DOWN
      self.player_rect.y += self.PLAYER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and self.is_valid('right'):  # RIGHT
      self.player_rect.x += self.PLAYER_VELOCITY
