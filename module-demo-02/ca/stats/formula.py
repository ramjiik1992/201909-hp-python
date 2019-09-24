

def freq(values):
    result={}
    for value in values: #loop 10000
        result[value]=result.get(value,0)+1 # 4-6
    
    return result