import sys
import getpass as p

#pyver=int(sys.version.split('.')[0])

pyver=sys.version_info.major


def read_str(prompt):
    if pyver>2:
        return input(prompt)
    else:
        return raw_input(prompt)

def read_int(prompt):
    return int(read_str(prompt))

def read_float(prompt):
    return float(read_str(prompt))

def read_eval(prompt):
    if pyver<3:
        return input(prompt)
    else:
        return eval(read_str(prompt))

def read_pass(prompt):
    
    return p.getpass(prompt)