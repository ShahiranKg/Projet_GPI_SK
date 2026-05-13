def parsePDB(file_name):
    RNA = 'RNA found in ' + file_name
    return RNA

def generate_dot_bracket(model):
    print(model)


with open(pdb_name,'r') as file:
    line = file.readline()
    while line[0:6].strip() != 'TER':
        if line[0:6].strip() == 'ATOM':
            x = float(line[30:38].strip())
            print(line)
        line = file.readline()