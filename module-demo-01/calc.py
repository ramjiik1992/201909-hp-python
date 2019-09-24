import sys

def main(name, *args):
    sum=0
    for value in args:
        sum+=float(value)

    print('sum {}'.format(sum))
    print('average {}'.format(sum/len(args)))


if __name__=='__main__':
    main(*sys.argv)
