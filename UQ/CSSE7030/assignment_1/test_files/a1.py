"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Peng YU}} ({{46635884}})"
__email__ = "peng.yu@uqconnect.edu.au"
__date__ = "31/08/2020"



# Write your code here (i.e. functions)

def select_word_at_random(word_select):
	'''
		Given the word_select is either "FIXED" 
	or "ARBITRARY" this function will return a 
	string randomly selected from WORDS_FIXED.txt 
	or WORDS_ARBITRARY.txt respectively. If 
	word_select is anything other then the expected
	input then this function should return None. 

	Parameters:
		word_select(str): A string representing 
			a FIXED or ARBITRARY word selection

	'''
	if word_select in ('ARBITRARY', 'FIXED'):
		word_all = load_words(word_select)
		select_word = word_all[random_index(word_all)]
		return select_word
	else :
		return None

def create_guess_line(guess_no, word_length):
	'''
	
	This function returns the string representing
		the display corresponding to the guess 
		number integer, guess_no. 

	Parmeters:
		
		guess_no(int): An integer reprsesnting 
			how many guesses the player has made
		
		word_length(int): An integer representing the 
			length of the word being guessed by 
			the player

	'''
	view = 'Guess *|'
	view_list = []
	for i in range(word_length):
		view += ' ' +  WALL_HORIZONTAL + ' ' + WALL_VERTICAL
	for times in range(word_length):
		view_temp = list(view)
		view_temp[6] = str(times + 1)
		start_num, last_num = GUESS_INDEX_TUPLE[word_length - 6][times]
		for i in range(start_num, last_num + 1):
			view_temp[ 4 * i + 9] = '*'
		view_list.append(''.join(view_temp))
	return view_list[guess_no-1]

def compute_value_for_guess(word, start_index, end_index, guess):
	'''
	
	Given the word select is, this function requires the 
		player to guess a substring which is created by 
		slicing the word from the strat_index up to and 
		including the end_index.

	Parmeters:
		word(str): The player has to guess the word.
		
		start_index(int) and end_index(int): The substring 
			to be guessed is determined by the fragment.
				
		guess(str): The guess attempt the player has made.

	Returns:
		(int): the player is awarded for a specific guess.
	
	'''
	points = 0
	for code, letter in enumerate(guess):
		if letter == word[start_index + code]:
			if letter in (VOWELS):
				points += 14
			elif letter in (CONSONANTS):
				points += 12
		elif letter in word[start_index:(end_index+1)]:
			points += 5
	return points

def display_guess_matrix(guess_no, word_length, scores):
	'''
	
	This function prints the progress of the game.

	Parmeters:
		guess_no(int): An integer reprsesnting 
			how many guesses the player has made

		word_length(int): An integer representing the 
			length of the word being guessed by 
			the player

		scores(tuple): A tuple containing all previous scores


	'''
	outprint = '       |'
	view_list = []
	for i in range(word_length):
		outprint += ' ' +  str((i+1)) + ' ' + WALL_VERTICAL
	line = WALL_HORIZONTAL * (len(outprint) + 1)
	for times in range(guess_no):
		view_list.append(create_guess_line((times+1),word_length))	
	for times in range(guess_no-1):
		view_list[times] += '   ' + str(scores[times]) + ' Points'
	print(outprint)
	print(line)
	for i in range(guess_no):
		print(view_list[i])
		print(line)

def main():
	"""
	Handles top-level interaction with user.
	"""
	# Write the code for your main function here
	input_difficulty = "Do you want a 'FIXED' or 'ARBITRARY' length word?: "
	view_list = []
	scores = ()
	word_select = None
	print(WELCOME, end = '\n')
	while True:
		input_action = input(INPUT_ACTION)
		if input_action in ('h', 's'):
			if input_action == 'h':
				print(HELP)
			while not word_select:
				difficulty_select = input(input_difficulty)
				word_select = select_word_at_random(difficulty_select)
			print('Now try and guess the word, step by step!!')
			for times in range(len(word_select)):
				input_guess_str = 'Now enter Guess %d: ' %(times + 1)
				start_num, last_num = GUESS_INDEX_TUPLE[len(word_select) - 6][times]
				view_list.append(create_guess_line((times+1),len(word_select)))				
				display_guess_matrix((times+1), len(word_select), scores)
				if times == (len(word_select) - 1):
					break
				else:
					while True:
						enter_guess = input(input_guess_str)
						if len(enter_guess) == last_num - start_num + 1:
							break
				points = compute_value_for_guess(word_select, start_num, last_num, enter_guess)
				scores += (points, )
			final_guess = input('Now enter your final guess. i.e. guess the whole word: ')
			if final_guess == word_select:
				print('You have guessed the word correctly. Congratulations.')
			else:
				print('Your guess was wrong. The correct word was \"%s\"' %word_select)
			break
		elif input_action == 'q':
			break
		else:
			print(INVALID)

if __name__ == "__main__":
	main()