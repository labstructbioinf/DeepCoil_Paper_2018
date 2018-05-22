import os
inps = os.listdir('in_profiles')
c = 0
for inp in inps:
	c += 1
	if not os.path.isfile('results/%s' % inp):
		os.system('python2.7 ~/predcchmm/pred.py in_profiles/%s > results/%s' % (inp, inp))
	print(c)
