from abc import ABCMeta, abstractmethod
from grid import Grid
import random


#An abstract class for the players to play the game. For this game it
#would be the player using the program and the computer.
class Player(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def choice(self):
		pass
	@abstractmethod
	def guess(self):
		pass
	@abstractmethod
	def make_grid(self):
		pass
	@abstractmethod
	def display_grid(self):
		pass

class User(Player):

	#Initizializing user object with an array for the user to choose which
	#point the computer has to guess.
	def __init__(self):
		self.user_point_opp = [0,0]
		self.user_grid = Grid("u")

	#Letting the user choose the point for the computer to guess on.
	def choice(self):
		print("You are going to pick the point for the player to guess!")
		while(True):
			try:
				point = raw_input("Think of a point. Now put it down (i.e. A5): ")
				if(len(point) != 2):
					raise Excpetion()
				row = int(point[1]) - 1
				if(row < 0 or row > 4):
					raise Exception()
				column = self.user_grid.y_axis[point[0].upper()]
				self.user_point_opp = [row,column]
				break
			except Exception:
				print("Invalid coordinate. Please, try again.")

	#The user is guessing which point on the grid is the computer's battleship.
	def guess(self):
		while(True):
			try:
				guess = raw_input("Guess the opponent's coordinate (i.e. A5): ")
				if(len(guess) != 2):
					raise Excpetion()
				row_guess = int(guess[1]) - 1
				if(row_guess < 0 or row_guess > 4):
					raise Exception()
				column_guess = self.user_grid.y_axis[guess[0].upper()]
				print("You guessed %s%s." %(guess[0].upper(),guess[1]))
				return [row_guess, column_guess]
			except Exception:
				print("Invalid coordinate. Please, try again.")

	#Making the grid for the user.
	def make_grid(self):
		self.user_grid.create_grid()

	#Printing the user's grid.
	def display_grid(self):
		print("\n  PLAYER'S BOARD\n")
		self.user_grid.print_grid()



class Computer(Player):

	#Initializing the computer object with an array for the  computer to choose
	#which point the player (user) has to guess.
	def __init__(self):
		self.computer_point_opp = [0,0]
		self.computer_grid = Grid("l")

	#Letting the computer the point for the player to guess on.
	def choice(self):
		row = random.randint(1,5) - 1
		column = self.computer_grid.y_axis[chr(random.randint(65,69))]
		self.computer_point_opp = [row,column]
		#self.computer_point_opp[0] = random.randint(1,5) - 1
		#self.computer_point_opp[1] = self.computer_grid.y_axis[chr(random.randint(65,69))]
		print("The computer picked a point for you to guess.")

	#The computer is guessing which point on the grid is the player's battleship.
	def guess(self):
		row_guess = random.randint(1,5) - 1
		letter = chr(random.randint(65,69))
		column_guess = self.computer_grid.y_axis[letter]
		print("The computer guessed %s%d." %(letter,row_guess+1))
		return[row_guess, column_guess]

	#Making the grid for the computer.
	def make_grid(self):
		self.computer_grid.create_grid()

	#Printing the grid for the computer.
	def display_grid(self):
		print("\n  COMPUTER'S BOARD\n")
		self.computer_grid.print_grid()