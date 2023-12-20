import math

# Given a number α, find rational numbers p/q such that |α - p/q| <= 1/q^2
# i.e. α=2.52 p/q = 5/2 α-p/q = 0.02 <= 1/4 = 0.25

def find_rational(α: float):
    """
    iterate on q, find the lowest integer p value that gives p/q = α 
    calculate lower and upper bounds
    this is our base p value, 
    now increment and if value found in between lower bound and upper bound add to list. Stop when greater than upper bound. 
    now decrement and if value found in between lower bound and upper bound add to list. Stop when less than lower bound.
    """
    HIGH_Q = 1001
    r_nums = []
    for q in range(1,HIGH_Q):
        p = math.floor(α*q)
        low_bound = α-(1/(q*q))
        high_bound = α+(1/(q*q))
        inc = 0
        while True:
            high_r = (p+inc)/q
            if high_r <= high_bound and high_r >= low_bound:
                r_nums.append((p+inc,q))
                inc+=1
            elif high_r < low_bound:
                inc+=1
            else:
                break 
        inc = 1 #set to one because we've already added when inc=0 above
        while True:
            low_r = (p-inc)/q
            if low_r >= low_bound and low_r <= high_bound:
                r_nums.append((p-inc,q))
                inc+=1
            elif low_r > high_bound:
                inc+=1
            else:
                break 
    return r_nums


if __name__ == '__main__':
    INPUT = (1+math.sqrt(5))/2
    r_nums = find_rational(INPUT)
    #formats input - setting same q values on the same line
    for i,set in enumerate(r_nums):
        if i<len(r_nums)-1:
            next_q = r_nums[i+1][1]
        else:
            next_q = -1
        p = set[0]
        q = set[1]
        if next_q != q:
            print(f'{p}/{q}')
        else:
            print(f'{p}/{q}', end=", ") 


    

