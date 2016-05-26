from game import Game

def main():
	gameplay = Game()
	gameplay.intro()
	gameplay.instructions()
	gameplay.game_loop()

if __name__ == '__main__':
	main()