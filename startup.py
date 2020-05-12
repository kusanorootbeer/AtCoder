import argparse
import os
import subprocess as sp

parser = argparse.ArgumentParser()
parser.add_argument('--dir_name', '-n', required=True, type=str)
parser.add_argument('--question', '-q', default=4, type=int)

args = parser.parse_args()

d_name = args.dir_name
q_num = args.question

if not os.path.exists(d_name):
    os.makedirs(d_name)
else:
    print("Already exsits the file")
    exit()


for f_n in range(ord('a'), ord('a')+q_num):
    f_name = chr(f_n) + '.py'
    cmd = ['touch', d_name+'/'+f_name]
    sp.run(cmd)
    cmd = ['cp', 'format.py', d_name+'/'+f_name]
    sp.call(cmd)
