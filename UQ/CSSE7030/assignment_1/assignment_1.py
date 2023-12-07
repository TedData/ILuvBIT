import random

def difficulty_file(difficulty):
	if difficulty == 'FIXED':
		file=open('WORDS_FIXED.txt')
		line=random.randint(1,2173)
	else:
		file=open('WORDS_ARBITRARY.txt')
		line=random.randint(1,10124)
	guess_word=file.readline()
	for temp in range(line-1):
		guess_word=file.readline()
	guess_word=guess_word[:-1]
	guess_word=guess_word.ljust(8)
	file.close()
	return guess_word
	











print('Welcome to the Criss-Cross Multi_Step Word Guessing Game!')

while True:
	initial_surface = input('\n\nEnter an input a ction. Choices are:\n\
s - start game\n\
h - get help on game rules\n\
q - quit game:\n')
	if initial_surface == 'h':
		print('Game rules - You have to guess letters in place of the asterixis.\n\
Each vowel guessed in the correct position gets 14 points.\n\
Each consonant guessed in the correct position gets 12 points.\n\
Each letter guessed correctly but in the wrong position gets 5 points.\n\
If the true letters were "dog", say, and you guessed "hod",\n\
you would score 14 points for guessing the vowel, "o", in the correct \n\
position and 5 points for guessing "d" correctly, but in the \n\
incorrect position. Your score would therefore be 19 points.')
	elif initial_surface == 'q':
		print('see you')
		break
	elif initial_surface == 's':
		while True:
			select_difficulty = input('Do you want a \'FIXED\' or\'ARBITRARY\' length word?: ')
			if select_difficulty in ('FIXED', 'ARBITRARY'):
				break
		guess_word = difficulty_file(select_difficulty)




		break		
	else:
		print('\nPlease enter a valid command.')







spilt='-'*41+'\n'
outprint='       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |\n'
outprint+=spilt 
view=[\
'Guess 1| * | * | - | - | - | - | - | - |   ',\
'Guess 2| - | * | * | * | - | - | - | - |   ',\
'Guess 3| - | - | - | - | * | * | * | * |   ',\
'Guess 4| - | - | - | * | * | * | - | - |   ',\
'Guess 5| - | - | - | * | * | * | * | - |   ',\
'Guess 6| - | - | - | - | - | * | * | * |   ',\
'Guess 7| - | - | * | * | * | * | * | * |   ',\
'Guess 8| * | * | * | * | * | * | * | * |   ']


outprint+=view[0]+'\n'+spilt
print(outprint)
for i in range(1,9):
	x=26
	y='Now enter Guess %d: '%(i)
	string=input(y)
	if i==1:
	outprint+=view[i]+'\n'+spilt
	print(outprint)





