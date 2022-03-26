import pygame
import math
from random import randint


class Enemy:

    def __init__(self, x, y, window, enemy_image, enemy_width, enemy_height, window_width, window_height,
                 enemy_velocity, cream_puff):
        self.WINDOW = window
        self.ENEMY_IMAGE = enemy_image
        self.ENEMY_WIDTH = enemy_width
        self.ENEMY_HEIGHT = enemy_height
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height
        self.ENEMY_VELOCITY = enemy_velocity
        self.enemy_rect = pygame.Rect(x, y, self.ENEMY_WIDTH, self.ENEMY_HEIGHT)
        self.cream_puff = cream_puff
        self.enemy_points = 0

    # Method for drawing the enemy on the screen
    def draw_enemy(self):
        self.WINDOW.blit(self.ENEMY_IMAGE, (self.enemy_rect.x, self.enemy_rect.y))

    # Checks if the player can move in the given direction
    def is_valid(self, side):
        if side == 'left':
            if self.enemy_rect.x > 0:
                return True
            else:
                return False
        if side == 'up':
            if self.enemy_rect.y > 0:
                return True
            else:
                return False
        if side == 'down':
            if self.enemy_rect.y + self.ENEMY_HEIGHT < self.WINDOW_HEIGHT:
                return True
            else:
                return False
        if side == 'right':
            if self.enemy_rect.x + self.ENEMY_WIDTH < self.WINDOW_WIDTH:
                return True
            else:
                return False

    # Sets the course of the enemy towards the cream puff
    def set_course(self):
        y_difference = self.cream_puff.cream_puff_rect.y - self.enemy_rect.y
        x_difference = self.cream_puff.cream_puff_rect.x - self.enemy_rect.x
        return [x_difference / math.fabs(x_difference + y_difference),
                y_difference / math.fabs(x_difference + y_difference)]

    def move_enemy(self):
        course = self.set_course()
        self.enemy_rect.x += course[0] * self.ENEMY_VELOCITY
        self.enemy_rect.y += course[1] * self.ENEMY_VELOCITY

    # Moves the cream puff when the player touches it
    def check_collisions(self):
        if self.cream_puff.cream_puff_rect.colliderect(self.enemy_rect):
            self.cream_puff.visible = False
            self.cream_puff.cream_puff_rect.x = randint(0, 850)
            self.cream_puff.cream_puff_rect.y = randint(0, 450)
            self.cream_puff.visible = True
            self.enemy_points += 1

