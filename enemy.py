from math import cos, pi, sin
import pygame
import pygame.draw as draw
from pygame.rect import Rect
import pygame.sprite as sprite
import pygame.surface as surface
from random import randint, uniform
from vector import Vector2 as Vector

"This is the \"Ba\" enemy from pathunstrom/ghostbowl"
class Enemy(sprite.DirtySprite):

    def __init__(self):
        super(Enemy, self).__init__()
        self.image = surface.Surface((30, 45))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.image.set_colorkey(COLOR_KEY)
        self.image.set_alpha(64)
        self.image.fill(COLOR_KEY)
        draw.circle(self.image, color, (15, 15), 15)
        body = Rect((0, 15, 30, 25))
        draw.rect(self.image,
                  color,
                  body)
        for count in xrange(4):
            count += 1
            draw.circle(self.image,
                        color,
                        (count * 6, 40),
                        5)
        self.facing = Vector(1, 0).normalize()
        self._x = x
        self._y = y
        self.speed = 20

    def update(self, delta):
        self._x += self.facing.x * self.speed * delta
        self._y += self.facing.y * self.speed * delta
        self.rect.center = self._x, self._y
