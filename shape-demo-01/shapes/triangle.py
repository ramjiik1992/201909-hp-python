def perimeter(s1,s2,s3):
    return s1+s2+s3 if s1>0 and s2>0 and s3>0 \
            and s1+s2>s3 and s1+s3>s2 \
            and s2+s3>s1 else None