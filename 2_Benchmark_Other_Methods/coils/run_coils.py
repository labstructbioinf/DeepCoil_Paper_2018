import pickle
id2seq = {}
aa1 = "ACDEFGHIKLMNPQRSTVWY"
from Bio import SeqIO
for record in SeqIO.parse("/home/db/pdb/pdb_seqres_clean.txt", "fasta"):
    nonstd_present = False
    for aa in str(record.seq):
        if aa not in aa1:
            nonstd_present = True
            break
    if not nonstd_present:
        id2seq[record.id] = str(record.seq)
import os
df = pickle.load(open('./../../1_Data_Preparation/out/pickle/data_all_74.p', 'rb'))
entries = set(df.index.tolist())
c = 0
print(len(entries))
for entry in entries:
	#os.system('python2.7 blastofas.py /home/db/psiblast/OUT_2_IT/%s.out %s.fasta > temp_files/hhfilter_output.a3m' % (entry, entry))
	#os.system('perl myhmmmake_PCoils.pl')
	if entry in id2seq.keys():
		c += 1
		print(c, entry)
		f = open('%s.fasta' % (entry), 'w')
		f.write('>%s\n' % entry)
		f.write('%s\n' % id2seq[entry])
		f.close()
		if not os.path.isfile('results/%s.coils_n14' % entry):
			#print("DUPA")
			os.system('/home/users/jludwiczak/PCOILS_v1.0.1/run_coils -nw -win 14 < %s.fasta > results/%s.coils_n14' % (entry, entry))
			os.system('/home/users/jludwiczak/PCOILS_v1.0.1/run_coils -nw -win 21 < %s.fasta > results/%s.coils_n21' % (entry, entry))
			os.system('/home/users/jludwiczak/PCOILS_v1.0.1/run_coils -nw -win 28 < %s.fasta > results/%s.coils_n28' % (entry, entry))
	os.system('rm %s.fasta' % entry)
