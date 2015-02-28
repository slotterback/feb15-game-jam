import pygame
from pygame.locals import K_w, K_a, K_s, K_d

from vector import Vector2


class Player(pygame.sprite.DirtySprite):
    def __init__(self, skills):
        pygame.sprite.DirtySprite.__init__(self)
        surface = pygame.Surface(50, 50)
        rect = pygame.draw.circle(surface, (0, 0, 255), (25, 25), 25)
        self.image = surface

        self.rect = rect

        self.skill_mod = 0
        self.skill_list = [[skills[0], skills[1]],
                           [skills[2], skills[3]]]  #[skillmod[skills]]

        self.move = Vector2(0, 0)
        self.x = 50
        self.y = 50
        self.current_speed = 50

        hp = 100  # At some point this will be hp - time

    def update(self, td):
        keys = pygame.key.get_pressed()
        w = keys[K_w]
        s = keys[K_s]
        a = keys[K_a]
        d = keys[K_d]
        x = a * -1 + d
        y = w * -1 + s
        self.move = Vector2(x, y)
        self.x += self.move.x * self.current_speed * td
        self.y += self.move.y * self.current_speed * td

    def attack(self, mouse):
        return self.skill_list[self.skill_mod][mouse]()

# ----------------------------------------------------------------------------
# Notes and testing functions.
# ----------------------------------------------------------------------------
"""
#Write function attack(toggle keypress):
	def attack(self, mouse):
		mousebutton1, mousebutton2 = 0, 0

		if self.skill_mod == 0:
			mousebutton1 = self.skill_list[0][0]
			bousebutton2 = self.skill_list[0][1]
		elif self.skill_mod == 1:
			mousebutton1 = self.skill_list[1][0]
			mousebutton2 = self.skill_list[1][1]

		return mousebutton1, mousebutton2"""


def skill1():
    print "You're using Skill1"


def skill2():
    print "You're using Skill2"


def skill3():
    print "You're using SKill3"


def skill4():
    print "You're using Skill4"

skill_list = [skill1, skill2, skill3, skill4]

character = Player(skill_list)

character.attack(1)

"""non-combat area loop
combat area loop

character model gets passed around

set all of this up in an init function:
player module:
	player sprite (and relevant update functions)
		don't worry about update function for right now


movement
toggles on the character - need to know if we're going in DIRECTION
1 skill mod - True or False* - Primary 2 buttons or alternate 2 buttons
Each different Skill - 4 skill slots


draw function:
surface - Dirty Sprite

Things to track:
Each Direction - is it moving
Skill modifier (toggle button for mouse click functionality)
4 individual skills - will all be initializers - either a function or a class (will be a sprite that has its own behaviors)


(In Player Module)"""

