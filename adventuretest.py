from sys import exit
from random import randint

def main():
	print """
	Welcome to AdventureTest! 
	To start off we'll ask a few questions and then recap. 
	Let's get started: \n"""
	
	name = raw_input("What is your name? \n>")
	
	player_class = raw_input ("\nChoose a class:\nWarrior\nThief\nMage \n>")
	player = create_class(player_class, name)
	
	print
	print "\nYour name is: %s" % player.name
	print
	print "Your class is: " + player.type
	print
	print "Your class stats are: \n" + str(player)

	while True:
		command = raw_input("What do you want to do? \n>")
		do_stuff(command)
	
	def death():
		quips = ["You Died. You must do well in real life.",
				"Nice JoB! You died, Jackass.",
				"Is that the shape of an L on your forehead?",
				"I have a small dingo better at this game than you."]
		print quips[randint(0, len(quips)-1)]
		exit(1)

def create_class(player_class, name):
	if player_class == "Mage":
		return PlayerClass(
			name = name,
			type = "Mage",
			health = 3,
			stre = 3,
			mana = 15,
			stealth = 5,
		)
	elif player_class == "Thief":
		return PlayerClass(
			name = name,
			type = "Thief",
			health = 5,
			stre = 2,
			mana = 5,
			stealth = 15,
		)
	elif player_class == "Warrior":
		return PlayerClass(
			name = name,
			type = "Warrior",
			health = 5,
			stre = 15,
			mana = 1,
			stealth = 5,
		)
	else:
		return False


class World():
	
	rooms = {
		'start_room': StartRoom(),
		'bear_room': BearRoom(),
		'other_room': OtherRoom(),
	}

	def __init__(self, player):
		self.player = player
		self.current_area = self.rooms['start_room']
	
	def where_can_i_go(self):
		print self.current_area.paths

start = StartRoom()

class Area():	
	paths = []

something = StartRoom()
some_other_thing = StartRoom()

class StartRoom(Area):
	paths = ['bear_room', 'other_room']
	
	def enter(self):
		print 'You enter a room! What do you do. \n>'


class BearRoom(Area):
	paths = ['start_room']
	
	def enter(self):
		pass


class OtherRoom(Area):
	paths = ['start_room']
	
	def enter(self):
		pass


class Item():

	def __init__(self, name):
		self.name = name

		
class PlayerClass():

	def __init__(self, name, type, health=3, stre=1, mana=15, stealth=5):
		self.name = name
		self.type = type	
		self.health = health
		self.stre = stre
		self.mana = mana
		self.stealth = stealth
		self.dead = False
	
	def take_hit(self, damage):
		self.health = self.health - damage
		
		if self.health <= 0:
			self.dead = True
	
	def __str__(self):
		return " Health: %d \n Strength: %d \n Mana: %d \n Stealth: %d" % (self.health, self.stre, self.mana, self.stealth)
		

if __name__ == '__main__':
	main()