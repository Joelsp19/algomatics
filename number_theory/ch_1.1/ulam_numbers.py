# Find the first n Ulam numbers, where n is a positive integer.
# The Ulam numbers Un. n = 1, 2, 3,... are defined as follows. We specify that u1 = 1 and u2 = 2. 
# For each successive integer m, m > 2, this integer is an Ulam number if and only if it can be written 
# uniquely as the sum of two distinct Ulam numbers. 


def binary_search(target,list,left,right):
    '''
    input: a target value, a list of values, a left pointer, a right pointer (initially left=0, right=len(list)-1)
    output: returns if the target is in the list
    '''
    if right < left:
        return False
    mid = (left+right)//2
    if list[mid] < target:
        return binary_search(target,list,mid+1,right)
    elif list[mid] > target:
        return binary_search(target,list,left,mid-1)
    else:
        return True


def find_ulam_nums(n: int):
    '''
    find the next integer say m(m=3 initially), and if we can construct this integer in more than one way then we don't add to list
    let a be the last value in the list- we have a target of m-a => binary search to get the target --> increment count
    decrement a till we get to the half way point or if the count is more than 1
    if count = 1 then we have one distinct way to make this number so add to the list
    '''

    ulam_nums = [1,2]
    m = 3 #represents a potential ulam number
    while len(ulam_nums) < n:
        l = len(ulam_nums)
        a = len(ulam_nums)-1
        count = 0
        #checks if more than one combo to make ulam number, adds to list if only one distinct way
        while a >= (l-1)/2:
            target = m-ulam_nums[a]
            if binary_search(target,ulam_nums[:a],0,a-1):
                count+=1
            if count > 1:
                break
            a-=1
        if count == 1:
            ulam_nums.append(m)
        m+=1
    return ulam_nums



if __name__ == '__main__':
    n = 100
    print(find_ulam_nums(n))
