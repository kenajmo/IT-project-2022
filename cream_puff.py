from random import randint

import pygame
import time
class CreamPuff:
  CREAM_PUFF_WIDTH = 50
  CREAM_PUFF_HEIGHT = 50
  cream_puff_rectangle = None
  visible = True

  # Constructor
  def __init__(self, pos_x, pos_y, window, cream_puff_image, player):
    self.cream_puff_rectangle = pygame.Rect(pos_x, pos_y, self.CREAM_PUFF_WIDTH, self.CREAM_PUFF_HEIGHT)
    self.WINDOW = window
    self.CREAM_PUFF_IMAGE = cream_puff_image
    self.player = player

  # Method to draw the cream puff
  def draw_cream_puff(self):
    if self.visible:
      self.WINDOW.blit(self.CREAM_PUFF_IMAGE, (self.cream_puff_rectangle.x, self.cream_puff_rectangle.y))

  # Moves the cream puff when the player touches it
  def check_collisions(self):
    if self.cream_puff_rectangle.colliderect(self.player.player_rect):
      self.visible = False
      self.cream_puff_rectangle.x = randint(0,900)
      self.cream_puff_rectangle.y = randint(0,500)
      self.visible = True
