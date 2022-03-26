import pygame


class CreamPuff:
    CREAM_PUFF_WIDTH = 50
    CREAM_PUFF_HEIGHT = 50
    cream_puff_rect = None
    visible = True

    # Constructor
    def __init__(self, pos_x, pos_y, window, cream_puff_image, player):
        self.cream_puff_rect = pygame.Rect(pos_x, pos_y, self.CREAM_PUFF_WIDTH, self.CREAM_PUFF_HEIGHT)
        self.WINDOW = window
        self.CREAM_PUFF_IMAGE = cream_puff_image
        self.player = player
        # self.enemy = enemy

    # Method to draw the cream puff
    def draw_cream_puff(self):
        if self.visible:
            self.WINDOW.blit(self.CREAM_PUFF_IMAGE, (self.cream_puff_rect.x, self.cream_puff_rect.y))
