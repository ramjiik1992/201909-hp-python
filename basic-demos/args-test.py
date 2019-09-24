
def my_func(x,*args,y=100):
    print('x={}\targs={}\ty={}'.format(x,args,y))

my_func(1,2,3,4, y=15)
my_func(1,2,3,4,5,6,  y= 7)
my_func(1,2,3)

