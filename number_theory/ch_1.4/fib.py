
#finds the first n terms with the fib condition and given starting values
def fib(first: int, second: int, n: int):
    terms = [first,second]
    for _ in range(n-2):
        next = first+second  
        terms.append(next)
        first,second = second,next    
    return terms

#finds all the fib numbers less than the limit given starting values as well
def fib_limit(first: int, second: int, limit: int):
    terms = [first,second]
    next = second
    while next < limit:
        next = first+second
        if next >= limit:
            return terms 
        else: 
            terms.append(next)
        first,second = second,next    
    return terms

#finds the sums of distinct fib numbers that represent a given positive integer
def zeckendorf(n: int):
    '''
    find fib till we pass this value
    subtract that value(last in list) then use as target
    keep going down till we find that value or less
    subtract and make as target
    continue till target = 0 (or if index = 1)
    '''
    sum_list = []
    target = n

    fib_list = fib_limit(1,1,n)
    sum_list.append(fib_list[-1])
    target -= fib_list[-1]
    i = len(fib_list)-3
    while target > 0 and i > 0:
        if fib_list[i]<=target:
            sum_list.append(fib_list[i])
            target -= fib_list[i]    
            i-=1 # ensures that a consecutive Fib number isn't picked     
        i-=1
    return sum_list


if __name__ == "__main__":
    print(fib(1,1,10))
    print(fib(1,3,10))

    print(fib_limit(1,1,49))
    print(zeckendorf(49))