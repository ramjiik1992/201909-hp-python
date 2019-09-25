class Triangle:
    pass

def is_valid(t):
    return  isinstance(t,Triangle) and t.valid
            

def perimeter(t):
    return t.s1 + t.s2 + t.s3 if is_valid(t) else None

def validate(t):
    t.valid=t.s1>0 and t.s2>0 and t.s3>0 \
            and t.s1+t.s2>t.s3 \
            and t.s1+t.s3>t.s2 \
            and t.s2+t.s3>t.s1


def create(s1,s2,s3):
    t=Triangle()
    t.s1,t.s2,t.s3=s1,s2,s3
    validate(t)
    return t
    