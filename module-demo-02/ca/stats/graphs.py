def histogram(freq):
    for (v,f) in freq.items() : # get all key and value
        print('{} | {} {}'.format(v,'==== ' * f,f))