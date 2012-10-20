from sys import exit
from random import randint

class Game(object):
	
	def __init__(self, start):
		self.quips = ["You Died. The Nyst Wind claims you.",
					"Game Over. The mystery remains.",
					]
		self.start = start
	
	def __main__():
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
		
		player_class = raw_input ("\nChoose a class:\nReporter\nDetective\nMarine \n>")
		player = create_class(player_class, name)
		
		print
		print "\nYour name is: %s" % player.name
		print
		print "Your class is: " + player.type
		print
		print "Your class stats are: \n" + str(player)

		#while True:
			#command = raw_input("\n What do you want to do? \n>")
			#Commands(command)
	def play(self):
		next = self.start
		
		while True:
			print "\n--------"
			room = getattr(self, next)
			next = room()	
			
	def death():	
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)

def create_class(player_class, name):
	if player_class == "Reporter":
		return PlayerClass(
			name = name,
			type = "Reporter",
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

#class Commands(command):
	#commands = {
		#'me': PlayerClass(name),
		#'stats': blahbalh(),
	
	
		#}
		
#class Area():	
	#paths = []

		
#class StartRoom(Area):
	#paths = ['second_room']
	
	#def enter(self):
		#print "You awaken in a room"
		#print "There is an exit to the North here"


#class SecondRoom(Area):
	#paths = ['start_room', 'first_jo_room', 'first_re_room', 'first_ma_room']
	
	#def enter(self):
		#pass

#class FirstJoRoom(Area):
	#paths = ['second_jo_room']
	
	#def enter(self):
		#pass
		
#class FirstReRoom(Area):
	#paths = ['second_re_room']
	
	#def enter(self):
		#pass

c#lass FirstMaRoom(Area):
	#paths = ['second_ma_room']
	
	#def enter(self):
		#pass

#class OtherRoom(Area):
	#paths = ['start_room']
	
	#def enter(self):
		#pass
		
	
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
		
class Item():

	def __init__(self, name):
		self.name = name

if __name__ == '__main__':
	main()