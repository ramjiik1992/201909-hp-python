
class Triangle:
    
    def is_valid(self):
        return  isinstance(self,Triangle) and self.valid


    def perimeter(self):
        return self.s1 + self.s2 + self.s3 if self.is_valid() else None

    def validate(self):
        self.valid=self.s1>0 and self.s2>0 and self.s3>0 \
                and self.s1+self.s2>self.s3 \
                and self.s1+self.s3>self.s2 \
                and self.s2+self.s3>self.s1


    def create(s1,s2,s3):
        t=Triangle()
        t.s1,t.s2,t.s3=s1,s2,s3
        t.validate()
        return t
    
    def info(self):
        return f'Triangle<{self.s1},{self.s2},{self.s3}>' if self.is_valid() else '<Invalid Triangle>'
    
    def draw(self,surface):
        if self.is_valid():
            print(f'{Triangle.info(self)} drawn on {surface}')
        
        
