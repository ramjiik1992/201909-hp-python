import shapes.circle as circle
from shapes.triangle import Triangle

def use_triangle(t):
    if t.is_valid():
        print(f'{t.info()} has perimeter {t.perimeter()}')
    else:
        print('Invalid Triangle')


def main():
   t1=Triangle.create(3,4,5)
   use_triangle(t1)

   t2=Triangle.create(3,4,12)
   use_triangle(t2)


main()