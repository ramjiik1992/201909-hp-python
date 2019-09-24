
def find_min(*values):
    min=values[0]      # creating a min
    #now I can't use buildint min() in this function
    for value in values[1:]:
        if value<min:
            min=value

    return min #this min is not overwriting global min

def label_print(message,value):
    print(f'{message}:{value}')


def main():
    
    r1= find_min(2,9,11,1,17) # create a local min that
    r2= min(2,9,11,1,17) # doesn't overwrite global min

    print='min of 2,9,11,1,17 is '; #overwrites the local print to become str

    label_print(print,r1)  #global print is still a function
    label_print(print,r2)

main()
