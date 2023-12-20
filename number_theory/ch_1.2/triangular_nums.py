def triangular_num(n: int):
    return (n)*(n+1)//2

def perfect_square(n: int):
    return n*n

def pentagonal_num(n: int):
    return (n)*(3*n-1)//2

def tetrahedral_num(n: int):
    return (n)*(n+1)*(n+2)//6

if __name__ == "__main__":
      
    n = 100
    print("triangular nums: ")
    print(triangular_num(n), end = " ")
    print ("")
    print ("perfect square: ")
    print(perfect_square(n), end = " ")
    print ("")
    print ("pentagonal nums: ")
    print(pentagonal_num(n), end = " ")
    print ("")
    print ("tetrahedral nums: ")
    print(tetrahedral_num(n), end = " ")

