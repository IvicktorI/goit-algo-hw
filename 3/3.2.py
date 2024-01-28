import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1001 or min>max or (max-min)<quantity or min==max or quantity<1:
        return []
    numbers=[]
    while len(numbers)<quantity:
        temp=random.randint(min,max)
        if temp not in numbers:
            numbers.append(temp)
    
    numbers.sort()
    return numbers

print(get_numbers_ticket(2,45,20))