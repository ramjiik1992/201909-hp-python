#This function can work on all python versions 2+

def histogram(freq,**kwargs):
    '''
    Plots text based horizontal histogram
    Input
        * freq : a dictionary where key is the item and value is its frquency
        * kwargs: defines customization parameters
            * design: design of a single unit of bar (default '==== ')
            * showValue: decides if frequency should be shown after bar (default: True)
            * align: decides if frequency values should be aligned (default: False)
                * Note: align is ignored if showValue is False
            * gap :decides if there should be a gap between each bar
            
    >>> histogram({2:6, 9:2, 4:4, 1:1 })
    2 | ==== ==== ==== ==== ==== ====  6
    9 | ==== ====  2
    4 | ==== ==== ==== ====  4
    1 | ====  1
    
    >>> histogram({2:6, 9:2, 4:4, 1:1 }, align=True)
    2 | ==== ==== ==== ==== ==== ====  6
    9 | ==== ====                      2
    4 | ==== ==== ==== ====            4
    1 | ====                           1
    
    >>> histogram({2:6, 9:2, 4:4, 1:1 }, design=':::')
    2 | :::::::::::::::::: 6
    9 | :::::: 2
    4 | :::::::::::: 4
    1 | ::: 1

    >>> histogram({2:6, 9:2, 4:4, 1:1 }, gap=True)
    2 | ==== ==== ==== ==== ==== ====  6
      |
    9 | ==== ====  2
      |
    4 | ==== ==== ==== ====  4
      |
    1 | ====  1
      |
      
    >>> histogram({2:6, 9:2, 4:4, 1:1 }, showValue=False,design=':::')  
    2 | :::::::::::::::::: 
    9 | :::::: 
    4 | :::::::::::: 
    1 | ::: 

    '''
    
    design=kwargs.get('design','==== ')
    showValue=kwargs.get('showValue',True)
    align=kwargs.get('align',False) if showValue else False
    gap=kwargs.get('gap',False)
    
    if align:
        #max calculation may take time. do it if you need it
        largestBarSize= max(freq.values()) * len(design)
    
    for (v,f) in freq.items() : # get all key and value
        bar=design*f
        if align:
            bar=bar.ljust(largestBarSize)
        label= f if showValue else ''
        
        v='{}'.format(v).rjust(5)
        
        print('{} | {} {}'.format(v,bar,label))
        if gap:
            print('{}'.format('|'.rjust(7)) )