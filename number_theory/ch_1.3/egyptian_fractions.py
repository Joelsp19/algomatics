# Given a rational number p/q, express p/q as an Egyptian fraction 

def egyptian_fraction(p: int, q: int):
    fracts = []
    den = 1
    if p>q:
        target = p/q - p//q
        fracts.append(p//q)
        fracts.append("|")
    else:
        target = p/q
    while target > 0.000001 and den<100000:
        if 1/den <= target:
            fracts.append(den)
            target -= 1/den
        den+=1
    return fracts

def improper_fraction(denoms: list):
    num = 0
    common_den = 1
    for den in denoms:
        common_den *= den
    for den in denoms:
        num += (common_den//den)
    return [num,common_den]


if __name__ == "__main__":
    denoms = (egyptian_fraction(355,113))
    print(denoms)
    if '|' in denoms:
        denoms = denoms[2:]
    print(improper_fraction(denoms))


