from maths import sum,average

def main():
    print('testing maths module',__name__)
    s=sum(1,2,3,4,5)
    a= average(1,2,3,4,5)
    print('values 1,2,3,4,5')
    print('sum is ',s)
    print('average is ',a)

if __name__=='__main__':
    main()
else:
    raise Exception('this is not an importable module!')