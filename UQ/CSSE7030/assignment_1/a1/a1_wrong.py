"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Peng YU}} ({{46635884}})"
__email__ = "peng.yu@uqconnect.edu.au"
__date__ = ""



# Write your code here (i.e. functions)
def select_word_at_random(word_select):
	if word_select in ('ARBITRARY', 'FIXED'):
		word_all = load_words(word_select)
		select_word = word_all[random_index(word_all)]
		return select_word
	else :
		return None

def create_guess_line(guess_no, word_length):
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
	print(WELCOME, end = '\n\n')
	while True:
		input_action = input(INPUT_ACTION)
		if input_action == 's':
			while True:
				difficulty_select = input('Do you want a \'FIXED\' or\'ARBITRARY\' length word?: ')
				if difficulty_select in ('FIXED', 'ARBITRARY'):
					word_all = load_words(difficulty_select)
					word_select = word_all[random_index(word_all)]
					break
			outprint = '       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | '
			view = 'Guess *| - | - | - | - | - | - | - | - | - |'
			outprint = outprint[:(4 * len(word_select) - 37)]
			view = view[:len(outprint) + 1] + '  '
			line = WALL_HORIZONTAL * (len(outprint) + 1)
			view_list = []

			print(word_select)

			print('Now try and guess the word, step by step!!')
			for times in range(len(word_select)):
				view_temp = list(view)
				view_temp[6] = str(times + 1)
				start_num, last_num = GUESS_INDEX_TUPLE[len(word_select) - 6][times]
				for i in range(start_num, last_num + 1):
					view_temp[ 4 * i + 9] = '*'
				view_list.append(''.join(view_temp))
				print(outprint)
				print(line)
				for i in range(times + 1):
					print(view_list[i])
					print(line)
				input_guess_str = 'Now enter Guess %d: ' %(times + 1)
				if times == (len(word_select) - 1):
					break
				else:
					while True:
						enter_guess = input(input_guess_str)
						if len(enter_guess) == last_num - start_num + 1:
							break
				points = 0
				for code, letter in enumerate(enter_guess):
					if letter == word_select[start_num + code]:
						if letter in (VOWELS):
							points += 14
						else:
							points += 12
					elif letter in word_select:
						points += 5
				view_list[times] += str(points) + ' Points'
			final_guess = input('Now enter your final guess. i.e. guess the whole word: ')
			if final_guess == word_select:
				print('You have guessed the word correctly. Congratulations.')
			else:
				print('Your guess was wrong. The correct word was \"%s\"' %word_select)
			break
		elif input_action == 'h':
			print(HELP)
		elif input_action == 'q':
			break
		else:
			print(INVALID)



if __name__ == "__main__":
	main()