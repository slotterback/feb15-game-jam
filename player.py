#Gets Saved under Game Folder ../Game/player.py

import pygame

class Player(pygame.sprite.DirtySprite):
	
	def __init__(self, skills):
		pygame.sprite.DirtySprite.__init__(self)
#		self.image = pygame.image.load("./images/image.png")

#		self.rect = self.image.get_rect()

#		directional true false
		self.skill_mod = 0
		self.skill_list = [[skills[0], skills[1]], [skills[2], skills[3]]] #[skillmod[skills]]

		#self.direction_list = [False, False, False, False] #Up, Down, Left Right
		self.current_speed = 
		hp = 100 # At some point this will be hp - time


	def update(self, td):
		td = 0 
		pygame.keys.get():
			pull out w a s d
			if w a s d: 
				self.vectorx = a * -1 + d
				self.vectory = w * -1 +s
				#1/rad2 = diagonals

				if vectorx and vectory:
					diagonal math
				
			else:
				pass

		self.rect.x = self.vectorx * self.speed * td
		self.rect.y = self.vectory * self.speed * td
		#pass

	#Piper's Version
	def attack(self, mouse):
		return self.skill_list[self.skill_mod][mouse]()



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


list = [skill1, skill2, skill3, skill4]


character = Player(list)

character.attack()



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

