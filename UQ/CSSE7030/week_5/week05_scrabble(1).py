SCRABBLE_VALUES = (
    ('a', 1), ('b', 3), ('c', 3), ('d', 2), ('e', 1),
    ('f', 4), ('g', 2), ('h', 4), ('i', 1), ('j', 8),
    ('k', 5), ('l', 1), ('m', 3), ('n', 1), ('o', 1),
    ('p', 3), ('q', 10), ('r', 1), ('s', 1), ('t', 1),
    ('u', 1), ('v', 4), ('w', 4), ('x', 8), ('y', 4),
    ('z', 10)
)

# Write your Scrabble code below
def read_scores(SCRABBLE_VALUES):
	temp={}
	for i in range(len(SCRABBLE_VALUES)):
		temp[SCRABBLE_VALUES[i][0]]=SCRABBLE_VALUES[i][1]
	return temp


def get_score(scores,word):
	point=0
	for i in word:
		point += scores.get(i,0)
	print(point)
scores = read_scores(SCRABBLE_VALUES)
#get_score(scores, 'quack')
#get_score(scores, '%fishing_')
resulet={}
for key, value in SCRABBLE_VALUES:
	resulet[key]=value
print(resulet)



