import recommendations as rs
from math import sqrt
p1='Lisa Rose'
p2='Toby'

def sim_distance(prefs, person_1, person_2):
	si={}
	
	for item in prefs[person_1]:
		if item in prefs[person_2]:
			si[item]=1
	# if they have no ratings in common, return 0
	if len(si)==0: return 0
