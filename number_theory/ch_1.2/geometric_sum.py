def geometric_sum(seq: list):
    n = len(seq)
    if n == 0:
        return 0
    elif n == 1:
        return seq[0]
    r =  seq[1]/seq[0]
    a = seq[0]
    if r==1:
        return (n+1)*(a)    
    return (a*r**(n+1) - a)/(r-1)

if __name__ == "__main__":
    a = 3
    r = -5
    n = 6
    seq = [a*(r**i) for i in range(n)]
    print("example geometric sum")
    print(geometric_sum(seq))

    n = 10000
    print("leibniz sequence telescoping to π/4") 
    leibniz = [1/(2*i+1) * (-1 if i%2 else 1) for i in range(n)]
    print(geometric_sum(leibniz))
    
