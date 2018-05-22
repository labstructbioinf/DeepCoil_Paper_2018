import os
cc_alph = 'VLIMFWYGAPSTCHRKQEND'
pssm_alph = 'ARNDCQEGHILKMFPSTWYV'
sl={}
for i,j in enumerate(pssm_alph):
	#print(i,j)
	sl[i] = cc_alph.find(j)
def pssm_to_profile(pssm,out=''):
	n_pssm =pssm.split('/')[-1]
	#print(n_pssm) 
	pssm = open(pssm,'r')
	out=open(out,'w')
	out.write('# the order of the 20 symbol is : V L I M F W Y G A P S T C H R K Q E N D'+'\n')
	for d in pssm:
		dm =[0]*20
		c=[j for j in d.strip().split(' ') if j]
		if len(c)>41:
			k=0
			for i in c[22:42]:
				#print("%.2f"  % float(int(i)/100.0))
				dm[sl[k]]="%.2f" % float(int(i)/100.0)
				k+=1
			st = ''
			for i in dm:
				st+=i + ' '
			out.write(st[:-1]+'\n')
	pssm.close()
	out.close()
