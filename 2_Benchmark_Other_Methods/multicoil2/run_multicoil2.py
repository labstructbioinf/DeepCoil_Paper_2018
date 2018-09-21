import pickle

import subprocess
import multiprocessing
import os


def os_cmd(cmd):
    subprocess.call([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #os.system(cmd)


def multiprocess(func, tasks, n_cores, tasks_per_core=1):
    stdout_queue = multiprocessing.Queue()
    pool = multiprocessing.Pool(
        processes=n_cores, initargs=[stdout_queue], maxtasksperchild=tasks_per_core)
    for i, data in enumerate(pool.imap(func, tasks), 1):
        print(i)
    pool.close()
    pool.join()

import os
df = pickle.load(open('./../../1_Data_Preparation/out/pickle/data_all_74.p', 'rb'))
entries = set(df.index.tolist())
id2seq = {}
for key, value in df.iterrows():
    id2seq[key] = value['sequence']
c = 0
#os.chdir('/home/users/jludwiczak/PCOILS_v1.0.1')
print(len(entries))
cmds = []
for entry in entries:
	c += 1
	#print(c, entry)
	f = open('in_fasta/%s.fasta' % (entry), 'w')
	f.write('>%s\n' % entry)
	f.write('%s\n' % id2seq[entry])
	f.close()
	cmds.append('java -jar ~/multicoil2/build/jar/MultiCoil2.jar -sfile in_fasta/%s.fasta -out results/%s.out' % (entry, entry))
	#os.system('rm %s.fasta' % entry)
multiprocess(os_cmd, cmds, n_cores=10)
