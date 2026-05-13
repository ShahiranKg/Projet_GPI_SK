#!/usr/bin/env python3

import sys
import RNA.utilis as utilis

if len(sys.argv) != 2:
    print('Error : Incorrect number of arguments')
    print('Usage')
    print('> + project_1.py + file pdb')
    exit()

pdb_name = sys.argv[1]

RNA = utilis.parsePDB(pdb_name)
utilis.generate_dot_bracket(RNA)

with open(pdb_name,'r') as file:
    line = file.readline()
    while line[0:6].strip() != 'TER':
        if line[0:6].strip() == 'ATOM':
            x = float(line[30:38].strip())
            print(line)
        line = file.readline()