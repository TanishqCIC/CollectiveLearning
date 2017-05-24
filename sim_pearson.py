import recommendations as rs
from math import sqrt
p1='Lisa Rose'
p2='Toby'

def sim_pearson(prefs, person_1, person_2):
	si={}

	for item in prefs[person_1]:
		if item in prefs[person_2]:
			si[item]=1
	n=len(si)
	if n==0: return 0

	sum1=sum([prefs[person_1][it] for it in si])
	sum2=sum([prefs[person_2][it] for it in si])
	
	# Add up the squares of all the differences
	sum_of_squares=sum([pow(prefs[person_1][item]-prefs[person_2][item],2)
		for item in prefs[person_1] if item in prefs[person_2]])
	return 1/(1+sum_of_squares)

print('Similarity between ', p1, ' and ', p2, ' is ', sim_distance(ds.critics, p1, p2))
