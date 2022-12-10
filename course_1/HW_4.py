from random import randint

"""
Task: Write the game "Guess the number", when writing the code, fulfill the following conditions:

the program accepts only integers, if the number is a float - message the user and end the game
output the number guessed by the user
if the user entered a string - notify the user and end the game
if the number is more than 10 - notify the user and end the game
if the number is less than 1 - notify the user and end the game
if the number is in the specified interval, but not guessed - inform the user that he "WAS CLOSE" and end the game
if the user guessed the number - CONGRATULATIONS to him and end the game
"""

type_error = "It's %s, I accept only integer"
wrong_range = "The number out of range 1-9"
win_congrats = "Congratulations, you guesses the number, it's %d"
lose_close = "Oh sad, you were so close"


# def is_float(line):
# 	try:
# 		float(line)
# 		return True
# 	except ValueError:
# 		return False


def play():
	text = input("Guess the number: ")
	try:
		number = int(text)

		if number < 1 or number > 9:
			print(wrong_range)
		else:
			print("You wrote:", number)

			if number == (r_numb := randint(1, 9)):
				print(win_congrats % r_numb)
			elif (number + 1) == r_numb or \
				(number - 1) == r_numb:
				print(lose_close)

			print(f"My number: {number}, random: {r_numb}")

	except ValueError:
		text = text.lower()
		# Works for 1.1 1,2 and "123,123,23.2323", but doesn't work for "."..
		# But it general I'd use method to check it...
		if ("." in text and text.count(".") == 1) \
			or ("," in text and text.count(",") == 1):
			print(type_error % "float")
		else:
			if text == "exit" or text == "e":
				exit()
			print(type_error % "text")


if __name__ == '__main__':
	while True:
		play()
