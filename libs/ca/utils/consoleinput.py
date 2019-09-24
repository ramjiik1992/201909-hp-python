import sys

if sys.version_info.major<3:
    input=raw_input   #replace input with raw_input for python 3-

def read_string(prompt,default=''):
    x=input(prompt)
    if x:
        return x
    else:
        return default


def read_int(prompt, default=0):
    x=read_string(prompt,None)
    if x is None:
        return default
    else:
        return int(x)

def read_float(prompt, default=0.0):
    x=read_string(prompt,None)
    if x is None:
        return default
    else:
        return float(x)


def read_boolean(prompt, default=False):
    x=read_string(prompt,None)

    if x is None:
        return default
    else:
        trues={'yes','y','ok','fine','accept','true','t'}
        falses={'no','n','false','f','cancel','reject'}

        x=x.lower()

        if x in trues:
            return True
        elif x in falses:
            return False
        else:
            return default