from sys import exit
from random import randint

class Game(object):
	
	def __init__(self, start):
		self.quips = ["You Died. The Nyst Wind claims you.",
					"Game Over. The mystery remains.",
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
		
	def hotel_room(self):
		print "test"
		
a_game = Game("hotel_room")
a_game.play()