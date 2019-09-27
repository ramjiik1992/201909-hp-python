class Person:
    def __init__(self):
         super(Person,self).__init__()
         print('Person created')
        
class Employee(Person):
    def __init__(self):
        super(Employee,self).__init__()
        print('Employee Created')

class TechnologyExpert:
    def __init__(self): 
        super(TechnologyExpert,self).__init__()
        print('Technology Expert created')
        
class Engineer(Employee,TechnologyExpert):
    def __init__(self):
        super(Engineer,self).__init__()
        print('Engineer Created')
        #Employee.__init__(self)
        #TechnologyExpert.__init__(self)







# out of classes


def main():
    e=Engineer()



main()

