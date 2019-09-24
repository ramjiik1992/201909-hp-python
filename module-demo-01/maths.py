
pi=3.141592

def sum(*args):
    result=0
    for value in args:
        result+=value

    return result


def average(*args):
    return sum(*args)/len(args)


def min(x,y): 
    if x<y :
        return x
    else:
        return y


