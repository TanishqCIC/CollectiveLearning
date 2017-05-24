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
	
		sum1Sq=sum([pow(prefs[person_1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[person_2][it],2) for it in si])

	pSum=sum([prefs[person_1][it]*prefs[person_2][it] for it in si])

	num=pSum-(sum1*sum2/n)
	
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0
	r=num/den
	return r

print('Similarity between ', p1, ' and ', p2, ' is ', sim_pearson(ds.critics, p1, p2))
