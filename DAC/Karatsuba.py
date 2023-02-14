def karatsuba(x,y):
    lenx = len(str(x))
    leny = len(str(y))

    if lenx == 1 or leny == 1:
        return x*y

    n = max(lenx,leny)
    nby2 = n//2

    a = x // 10**nby2
    b = x % 10 ** nby2
    c = y // 10**nby2
    d = y % 10 ** nby2

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    adplusbc = karatsuba(a+b,c+d) - ac - bd

    product = ac * 10**(2*nby2) + adplusbc * 10 ** nby2 + bd
    return product


print(karatsuba(12,30))

