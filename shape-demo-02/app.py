import shapes.circle as circle
import shapes.triangle as triangle 

def use_triangle(t):
    if triangle.is_valid(t):
        print(f'Triangle<{t.s1},{t.s2},{t.s3}> has perimeter {triangle.perimeter(t)}')
    else:
        print('Invalid Triangle')


def main():
   t1=triangle.create(3,4,5)
   use_triangle(t1)

   t2=triangle.create(3,4,12)
   use_triangle(t2)


main()