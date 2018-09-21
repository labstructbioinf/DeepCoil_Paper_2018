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
os.chdir('/home/users/jludwiczak/marcoil')
for entry in entries:
	c += 1
	print(c, entry)
	f = open('%s.fasta' % (entry), 'w')
	f.write('%s\n' % id2seq[entry])
	f.close()
	os.system('./marcoil -C +dssSl %s.fasta' % entry)
	os.system('rm %s.fasta' % entry)
	os.system('mv ProbListPSSM /home/users/jludwiczak/DeepCoil/benchmark/marcoil/results/%s.problist' % entry)
	os.system('mv DomainsPSSM /home/users/jludwiczak/DeepCoil/benchmark/marcoil/results/%s.domains' % entry)
