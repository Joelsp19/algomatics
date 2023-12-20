import math
#  Given a number α, find its spectrum sequence
# spectrum sequence: The spectrum sequence of a real number α is the sequence that has [nα] as its nth term. 

def find_spectrum_sequence(α: float, n: int):
    '''
    simply find the floor of the integer for all numbers d from 1-n -> dα
    '''
    spectrum_seq = []
    for d in range(1,n+1):
        spectrum_seq.append(math.floor(d*α))
    return spectrum_seq

if __name__ == '__main__':
    α = (1+math.sqrt(5))/2
    α2 = math.e
    n = 100
    print(find_spectrum_sequence(α,n))
    print(find_spectrum_sequence(α2,n))

