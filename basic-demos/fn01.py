def do_nothing():
    pass

def say_hello(name):
    print(f'Hello {name}, Welcome to Python!')

def add(x,y):
    return x+y

x=do_nothing()  #returns None
print(x,id(x))

y=say_hello('Vivek') # will print message but return None
print(y,id(y))

z=add(20,40)
print(z)

a=add('hello','world')
print(a)

b=add('hello',29)
print(b)


