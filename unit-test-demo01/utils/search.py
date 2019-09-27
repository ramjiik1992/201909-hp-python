

def search(fnMatch, *args):
    if len(args)==1 :
        args=args[0]

    for value in args:
        if fnMatch(value):
            yield value