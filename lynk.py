#lynk itnerview question
#
#@author Gabriel Lando
#
#Given a wordlist (newline separated file of words) and given two words as input parameters, 
#find the minimal path from the first word to the second in the word list where each step can 
#be only of Levenshtein distance 1 (a change, insertion or deletion of a single letter).
#
#reference 1: https://en.wikipedia.org/wiki/Levenshtein_distance
#reference 2: http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

# read dictionary file
#words = open(DICTIONARY, "rt").read().split();

def dist_copmute(word1, word2):
	#Set the lengths and construct matrix T using m rows and n columns
	##Fill using bottom up dp aproach
	m = len(word1) + 1
	n = len(word2) + 1
	T = [[0 for x in range(n)] for x in range(m)]

	for i in range(n):
		T[0][i] = i
	for i in range(m):
		T[i][0] = i
    
    #insterts, deletions and substitutions
	for i in range(1, m):
		for j in range(1, n):
			if word1[i-j] == word2[j-1]:
				T[i][j] = T[i-1][j-1]
			else:
				T[i][j] = 1 + min(T[i-1][j-1], T[i-1][j], T[i][j-1])

	getEdited(T, word1, word2)
	return T[m-1][n-1]

def getEdited(T, word1, word2):
	#prints what was edited
	#contains provision for empty strings
	i = len(T) - 1
	j =len(T[0]) -1
	while True:
		if i == 0 or j == 0:
			break
		if word1[i-1] == word2[j-1]:
			i = i-1
			j = j-1
		elif T[i][j] == T[i-1][j-1] + 1:
			print "Edit %s in the second word to %s in the first word" %(word2[j-1], word1[i-1])
			i = j-1
			j = i-1
		elif T[i][j] == T[i-1][j] + 1:
			print "Delete %s from the first word" %(word1[i-1])
			i = i-1
		elif T[i][j] == T[i][j] + 1:
			print "Delete %s in the second word" %(word2[j-1])
			j = j-1


if __name__ == '__main__':
	answer = dist_copmute(list('test'), list('trist'))
	print(answer)