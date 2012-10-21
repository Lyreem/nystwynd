from sys import exit
from random import randint

class Game(object):
	

	
	def __init__(self, start):
	
		
		self.player = None
		self.quips = ["You Died. The Nyst Wind claims you.",
					"Game Over. The mystery remains.",
					"The Nyst Wind has blinded you. Unfortunate.",
					]
		self.start = start

	def play(self):
		next = self.start
		
		while True:
			print "\n--------"
			room = getattr(self, next)
			next = room()	
			
	def death(self):	
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)
	
	def main(self):
		
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
		Welcome to AdventureTest(replace this before live)! 
		To start off we'll ask a few questions and then recap. 
		Let's get started: \n"""
		
		
		
		name = raw_input("What is your name? \n>")
		player_class = raw_input ("\nChoose a class:\nReporter\nDetective\nMarine \n>")
		self.player = create_class(player_class, name)
				
		print
		print "Your class stats are: \n" + str(self.player)
		
		mcguffin = True
		if mcguffin == True:
			return 'hotel_room'
		else:
			return 'death'
			
	def hotel_room(self):
		print """
		You are in a hotel room, with no recollection of how you got there.
		The pounding of your head keeps tempo with a moaning wind outside, and
		an eerie light seeps through the tattered curtains. Your phone beeps, and
		reminds you that it is October 31st, before the battery dies.
		You should leave this room."""
		action =  raw_input("> ") 
		if action == 'leave room':
			return 'hall_way'
		elif action == 'look window':
			print """
			You part the curtains and see a swirling vortex of wind, full of debris and unearthly colors.
			You hastily close the curtains, filled with a feeling of dread and despair."""
			return 'hotel_room'
		else:
			print "You really should leave the room!"
			return 'hotel_room'
		
	def hall_way(self):
		print """
		You stagger out of your room into a dingy hallway, the door slamming shut behind you.
		As you grip the door frame for stability while the world spins around you, 
		the Nyst outside the walls makes a sound akin to a pallbearer mourning.
		\nWhat Do You Do?"""
		action = raw_input("> ")
		if action == 'look':
			if self.player.type == "Reporter":
				print "There is a door in front of you labelled: Reporter. What Do You Do?"
				if raw_input("> ") == 'open door':
					return 'reporter_1'
				else:
					print 'try again'
					return 'hall_way'
			elif self.player.type == "Detective":
				print "There is a door in front of you labelled: Detective. What Do You Do?"
				if raw_input("> ") == 'open door':
					return 'detective_1'
				else:
					print 'try again'
					return 'hall_way'
				
			elif self.player.type == "Marine":
				print "There is a door in front of you labelled: Marine. What Do You Do?"
				if raw_input("> ") == 'open door':
					return 'marine_1'
				else:
					print 'try again'
					return 'hall_way'
			else:
				print 'You are Blinded, and cannot proceed'
		else:
			print "Perhaps you should look around?"
			return 'hall_way'
			
			
	def reporter_1(self):
		print """
		As you step through the door, you remember that you came to this small town to
		write an expose on the annual event referred to as the "Nyst Wind".
		After a fruitless day questioning the locals regarding this happening,
		you retired to your hotel room, and fell into a deep slumber..."""
		print """
		The room is wallpapered in famous news clippings of strange happenings around the world. 
		There are stairs up, stairs down, and what appears to be a balcony."""
		action = raw_input("> ")
		if action == 'up stairs':
			return 'up_stair'
		elif action == 'down stairs':
			return 'down_stairs'
		elif action == 'balcony':
			return 'balcony'
		else:
			print "The Nyst Wind wouldn't want you to do that. Why would you?"
			return 'reporter_1'
		
	def detective_1(self):
		print """
		Stepping through the door, it dawns on you that you've been here before.
		A year ago, you were on a case involving mysterious disappearances in a small midwestern town.
		You had evidence of old-world cultists being tied up in it, 
		but could never definitively pin it on anyone.
		Yesterday, you returned to the town on the trail of fresh evidence...
		"""
		print """
		The room is vague, and devoid of form or substance. 
		There are stairs up, stairs down, and what appears to be a balcony."""
		action = raw_input("> ")
		if action == 'up stairs':
			return 'up_stair'
		elif action == 'down stairs':
			return 'down_stairs'
		elif action == 'balcony':
			return 'balcony'
		else:
			print "The Nyst Wind wouldn't want you to do that. Why would you?"
			return 'detective_1'
		
	
	
	def marine_1(self):
		print """
		As you pass the lintel, it's as if you have surfaced from drowning!
		You immediately go into defensive crounch and survey your surroundings, 
		remembering the danger you are in.
		Sent here by the government, your mission is to prevent the townsfolk 
		from summoning a creature from beyond, to stop them from giving flesh 
		to the Nyst Wind. A possibility too horrific to consider.
		"""
		print """
		Blood runs down the walls of the room, pooling in the center of the floor.
		Within the pool, you can see snippets of people writhing in agony.
		There are stairs up, stairs down, and what appears to be a balcony.
		"""
		
		action = raw_input("> ")
		if action == 'up stairs':
			return 'up_stair'
		elif action == 'down stairs':
			return 'down_stairs'
		elif action == 'balcony':
			return 'balcony'
		else:
			print "The Nyst Wind wouldn't want you to do that. Why would you?"
			return 'marine_1'
			
	def up_stair(self):
		
	def down_stair(self):
		
	def Balcony(self):
	
	
		
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


if __name__ == '__main__':
	a_game = Game("main")
	a_game.play()	