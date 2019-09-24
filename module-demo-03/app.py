
import ca.utils.consoleinput as kb;
from ca.stats.formula import freq
from ca.stats.graphs import histogram


def main():
    run=True
    while run:
        numbers=[]
        while True:
            
            number=kb.read_int("number?",None)
            if number==None:
                break
            numbers.append(number)

        f=freq(numbers)
        histogram(f)

        run=kb.read_boolean('continue?',False)
    


main()