import time

class Grid(object):

	#A "static" dictionary variable that will transform the letter
	#that the user input into a number for the grid.
	y_axis = {"A":0, "B":1, "C":2, "D":3, "E":4}

	#A constructor for the Grid object. It will initizialize a 2D
	#grid. The constructor also takes a parameter called "case", which
	#will take an uppercase or lowercase letter to construct the grid
	def __init__(self,case):
		self.g = []
		self.case = case

	#A grid, with either lowercase letters or uppercase letters, will
	#be created when calling this method.
	def create_grid(self):
		if self.case == 'u':
			self.g = [["O" for j in range(5)] for i in range(5)]
		elif self.case == 'l':
			self.g = [["o" for j in range(5)] for i in range(5)]
		else:
			pass

	#The grid will be printed when calling this method.
	def print_grid(self):
		letter = 65
		print("   1  2  3  4  5\n")
		for i in self.g:
			print(chr(letter) + " "),
			for j in i:
				print(j + " "),
			print("\n")
			time.sleep(0.05)
			letter += 1