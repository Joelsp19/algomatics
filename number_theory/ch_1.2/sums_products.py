from triangular_nums import * 

def summorial(seq: list):
    total = 0
    for elem in seq:
        total += elem
    return total

def factorial(seq: list):
    total = 1
    for elem in seq:
        total *= elem
    return total
    
if __name__ == "__main__":
    n = 3
    seq_dict= {}
    integer_sequence = [i for i in range(1,n+1)]
    triangular_sequence = [triangular_num(i) for i in range(1,n+1)]
    perfect_square_sequence = [perfect_square(i) for i in range(1,n+1)]
    pentagonal_sequence = [pentagonal_num(i) for i in range(1,n+1)]
    tetrahedral_sequence = [tetrahedral_num(i) for i in range(1,n+1)]
    seq_dict["integer_sequence"] = (integer_sequence)
    seq_dict["triangular_sequence"] = (triangular_sequence)
    seq_dict["perfect_square_sequence"] = (perfect_square_sequence)
    seq_dict["pentagonal_sequence"] = (pentagonal_sequence)
    seq_dict["tetrahedral_sequence"] = (tetrahedral_sequence)
    
    print("summorial")
    for key in seq_dict:
        print(key, end=", ")
        print(summorial(seq_dict[key]))

    print("")
    print("factorial")
    for key in seq_dict:
        print(key, end=", ")
        print(factorial(seq_dict[key]))

            
    