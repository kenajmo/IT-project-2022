import pygame
class CreamPuff:
  CREAM_PUFF_WIDTH = 50
  CREAM_PUFF_HEIGHT = 50
  cream_puff_rectangle = None
  visible = True

  def __init__(self, pos_x, pos_y, window, cream_puff_image, character):
    self.cream_puff_rectangle = pygame.Rect(pos_x, pos_y, self.CREAM_PUFF_WIDTH, self.CREAM_PUFF_HEIGHT)
    self.WINDOW = window
    self.CREAM_PUFF_IMAGE = cream_puff_image
    self.character = character

  def draw_cream_puff(self):
    if self.visible:
      self.WINDOW.blit(self.CREAM_PUFF_IMAGE, (self.cream_puff_rectangle.x, self.cream_puff_rectangle.y))

  def check_collisions(self):
    if self.cream_puff_rectangle.colliderect(self.character.character_rect):
      self.visible = False
