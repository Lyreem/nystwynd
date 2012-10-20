from sys import exit
from random import randint

def main():
	print """
@@@  @@@  @@@ @@@   @@@@@@   @@@@@@@  
@@@@ @@@  @@@ @@@  @@@@@@@   @@@@@@@  
@@!@!@@@  @@! !@@  !@@         @@!    
!@!!@!@!  !@! @!!  !@!         !@!    
@!@ !!@!   !@!@!   !!@@!!      @!!    
!@!  !!!    @!!!    !!@!!!     !!!    
!!:  !!!    !!:         !:!    !!:    
:!:  !:!    :!:        !:!     :!:    
 ::   ::     ::    :::: ::      ::    
::    :      :     :: : :       :     


@@@  @@@  @@@  @@@ @@@  @@@  @@@  @@@@@@@   
@@@  @@@  @@@  @@@ @@@  @@@@ @@@  @@@@@@@@  
@@!  @@!  @@!  @@! !@@  @@!@!@@@  @@!  @@@  
!@!  !@!  !@!  !@! @!!  !@!!@!@!  !@!  @!@  
@!!  !!@  @!@   !@!@!   @!@ !!@!  @!@  !@!  
!@!  !!!  !@!    @!!!   !@!  !!!  !@!  !!!  
!!:  !!:  !!:    !!:    !!:  !!!  !!:  !!!  
:!:  :!:  :!:    :!:    :!:  !:!  :!:  !:!  
 :::: :: :::      ::     ::   ::   :::: ::  
  :: :  : :       :     ::    :   :: :  :   \n\n"""

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
		command = raw_input("\n What do you want to do? \n>")
		do_stuff(command)
	
	def death():
		quips = ["You Died. You must do well in real life.",
				"Nice Job! You died, Jackass.",
				"Is that the shape of an L on your forehead?",
				"I have a small dingo better at this game than you."]
		print quips[randint(0, len(quips)-1)]
		exit(1)

def create_class(player_class, name):
	if player_class == "Reporter":
		return PlayerClass(
			name = name,
			type = "eporter",
			health = 3,
			stre = 3,
			mana = 15,
			stealth = 5,
		)
	elif player_class == "Detective":
		return PlayerClass(
			name = name,
			type = "Detective",
			health = 5,
			stre = 2,
			mana = 5,
			stealth = 15,
		)
	elif player_class == "Marine":
		return PlayerClass(
			name = name,
			type = "Marine",
			health = 5,
			stre = 15,
			mana = 1,
			stealth = 5,
		)
	else:
		return False
		
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

class World():
	
	rooms = {
		'start_room': StartRoom(),
		'second_room': SecondRoom(),
		'other_room': OtherRoom(),
		'first_jo_room': FirstJoRoom(),
		'first_re_room': FirstReRoom(),
		'first_ma_room': FirstMaRoom(),
	}

	def __init__(self, player):
		self.player = player
		self.current_area = self.rooms['start_room']
	
	def where_can_i_go(self):
		print self.current_area.paths

start = StartRoom()

class Area():	
	paths = []

		
class StartRoom(Area):
	paths = ['second_room']
	
	def enter(self):
		pass


class SecondRoom(Area):
	paths = ['start_room', 'first_jo_room', 'first_re_room', 'first_ma_room' ]
	
	def enter(self):
		pass

class FirstJoRoom(Area):
	paths = ['second_jo_room']
	
	def enter(self):
		pass
		
class First_Re_Room(Area):
	paths = ['second_re_room']
	
	def enter(self):
		pass

class First_Ma_Room(Area):
	paths = ['second_ma_room']
	
	def enter(self):
		pass

class OtherRoom(Area):
	paths = ['start_room']
	
	def enter(self):
		pass
		
		
class Item():

	def __init__(self, name):
		self.name = name

if __name__ == '__main__':
	main()