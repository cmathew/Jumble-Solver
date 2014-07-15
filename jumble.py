#written for Python 3.x by Chris Mathew

from string import ascii_letters

def get_word_value(word):
	#add up character values
	#to convert string to int
	word_hash = 0
	for c in word:
		word_hash += ord(c)
	return word_hash

#required dictionary plain text file
f = open("en_US.dic", "r")
words = dict()

for line in f:
	#dictionary has some data for word permutations
	#we only want the base word
	word_pieces = line.split('/')
	word = word_pieces[0]
	
	#don't include any contractions or one-letter words
	if word.find("'") != -1 or len(word) == 1:
		continue
	
	word_hash = get_word_value(word)
	
	#add word to our table
	#indexed by its hash value
	if not word_hash in words:
		words[word_hash] = [];
	words[word_hash].append(word)
f.close()

#verify that all letters are letters
all_letters = False
jumble_letters = []
while not all_letters:
	jumble_string = input("Enter a string of letters: ")
	all_letters = True
	jumble_letters = []
	for c in jumble_string:
		jumble_letters.append(c)
		if c not in ascii_letters:
			all_letters = False

matches = set()
def check_word_match(word_candidate, jumble_letters):
	#check if hash of string matches that of a real word
	word_hash = get_word_value(word_candidate)
	if word_hash in words:
		#check words for match with string
		for w in words[word_hash]:
			if w == word_candidate:
				matches.add(word_candidate)
				
	#keep building words, testing them
	for i in range(0, len(jumble_letters)):		
		new_letter = jumble_letters[i]
		jumble_letters_remaining = jumble_letters.copy()		
		del jumble_letters_remaining[i]
		check_word_match(word_candidate + new_letter, jumble_letters_remaining)
	
#build all permutations of the input string
check_word_match('', jumble_letters)

print(matches)
