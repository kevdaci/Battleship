from players import User,Computer
import time
import random

class Game(object):

	#A constructor to initialize the game. The two player objects are initialized and
	#their grids are constucted.
	def __init__(self):
		self.u = User()
		self.u.make_grid()
		self.comp = Computer()
		self.comp.make_grid()

	#The intro for the game.
	def intro(self):
		print("******************************************************************************")
		print("*	                                                                     *")
		print("*                                   Battleship!                              *")
		print("*	                                                                     *")
		print("******************************************************************************\n")

	#The game instructions.
	def instructions(self):
		print("   1  2  3  4  5\n")
		print("A  O  O  O  O  O\n")
		print("B  O  O  O  O  O\n")
		print("C  O  O  O  O  O\n")
		print("D  O  O  O  O  O\n")
		print("E  O  O  O  O  O\n")

		print("Welcome to the game of battleship! You will be playing against a computer")
		print("to test your intelligence. Above is a grid with a bunch of Os. You will be ")
		print("racing the computer. Who ever hits the opponent's battleship first will win")
		print("the game.")

		print("Look at the grid. The grid has a coordinate system. The top column shows the" )
		print("numbers 0-4. The first column also had the numbers 0-4. You will choose to" )
		print("locate your battleship for you computer opponent to guess on. You will choose")
		print("the coordinate based on the row number and the column number. This will also" )
		print("be the way for you to guess the opponent's battleship. Good luck and have fun!")
		print("_______________________________________________________________________________\n")

	#Letting the players choose location of their ships on the grid.
	def players_choose_point(self):
		self.u.choice()
		self.comp.choice()

	#This helper method will choose which player will go first.
	def first(self):
		return random.randint(0,1)

	#This method will play the Battleship game with the user winning the coin toss
	#and gets to choose his/hers opponent's coordinates first.
	def player_first(self):
		while True:
			self.u.display_grid()
			user_guess = self.u.guess();
			time.sleep(1)
			if user_guess[1] == self.comp.computer_point_opp[0] and user_guess[0] == self.comp.computer_point_opp[1]:
				print("You sunk the computer's ship! You won! ")
				time.sleep(1)
				break
			else:
				if self.u.user_grid.g[user_guess[1]][user_guess[0]] == "X":
					print ("You already guessed that point!")
				else:
					print("You missed the computer's ship!")
					self.u.user_grid.g[user_guess[1]][user_guess[0]] = "X"

			time.sleep(1)
			self.comp.display_grid()
			computer_guess = self.comp.guess()
			time.sleep(1)
			if computer_guess[1] == self.u.user_point_opp[1] and computer_guess[0] == self.u.user_point_opp[0]:
				print("The computer sunk your ship! You lost!")
				time.sleep(1)
				break
			else:
				if self.comp.computer_grid.g[computer_guess[1]][computer_guess[0]] == "x":
					print("The computer guessed that point! You get another shot!")
				else:
					print("The computer misssed your ship! You are still alive!")
					self.comp.computer_grid.g[computer_guess[1]][computer_guess[0]] = "x"
				time.sleep(1)

	#This method will play the Battleship game with the computer winning the coin toss
	#and gets to choose its opponent's coordinates first.
	def computer_first(self):
		while True:
			self.comp.display_grid()
			computer_guess = self.comp.guess()
			time.sleep(1)
			if computer_guess[1] == self.u.user_point_opp[1] and computer_guess[0] == self.u.user_point_opp[0]:
				print("The computer sunk your ship! You lost!")
				time.sleep(1.5)
				break
			else:
				if self.comp.computer_grid.g[computer_guess[1]][computer_guess[0]] == "x":
					print("The computer guessed that point! You get another shot!")
				else:
					print("The computer misssed your ship! You are still alive!")
					self.comp.computer_grid.g[computer_guess[1]][computer_guess[0]] = "x"

			time.sleep(1)
			self.u.display_grid()
			user_guess = self.u.guess();
			time.sleep(1)
			if user_guess[1] == self.comp.computer_point_opp[0] and user_guess[0] == self.comp.computer_point_opp[1]:
				print("You sunk the computer's ship! You won! ")
				time.sleep(1)
				break
			else:
				if self.u.user_grid.g[user_guess[1]][user_guess[0]] == "X":
					print ("You already guessed that point!")
				else:
					print("You missed the computer's ship!")
					self.u.user_grid.g[user_guess[1]][user_guess[0]] = "X"
				time.sleep(1)

	#The game running.
	def game_loop(self):
		self.players_choose_point()
		if self.first():
			print("\nA coin was tossed to see who goes first, and you won the coin toss!")
			time.sleep(1.5)
			self.player_first()
		else:
			print("\nA coin was tossed to see who goes first, and the computer won the coin toss!")
			time.sleep(1.5)
			self.computer_first()
