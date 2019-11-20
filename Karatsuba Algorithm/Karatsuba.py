import math


# This is an implementation of the Karatsuba multiplication algorithm
# The basic concept is in x * y we can split both x and y in half
# (for example if x = 1234 then a= 12 and b= 34) and we plug these into
# (10**n)*ac + (10 ** (n/2))(ad + bc) + bd, with recursive calls on each
# multiplication until we arrive at the base case where both x and y are
# 1 digit. This implementation is not a complete implementation, because
# we still use normal multiplication for multiplying constants such as (10**n)
def karatsuba(x, y):
    #   check for multiplying by zero
    if x == 0 or y == 0:
        return 0
    # check which number is larger so that we know which one to use to determine
    # the number of digits. This is needed to split up the numbers and for the actual
    # karatsuba equation.
    if x < y:
        n = int(math.log10(x))+1
    else:
        n = int(math.log10(y))+1
    # This is the base case where is both x and y are a single digit, we multiply and return the product
    if n <= 1:
        return x * y
    # check if n is odd
    if n % 2 > 0:
        n -= 1
    # the divisor here is used to split x and y into halves
    # and also is used at the end as a multiplicand
    divisor = 10**(n//2)
    a = x // divisor
    b = x % divisor
    c = y // divisor
    d = y % divisor
    p = a + b
    q = c + d
    # The recursive calls to get the products necessary for the equation
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    # pq = ac + bd + ab + bc or (a+b)(c+d)
    pq = karatsuba(p, q)
    # (ad+bc) = pq - ac - bd
    adbc = pq - ac - bd
    return (ac * (10**n)) + (adbc * divisor) + bd


first_num = 1234567891011121314151617181920212223242526272829303132333435363
second_num = 1357911131517192123252729313335373941434547495153555759616365676
print(karatsuba(first_num, second_num))
# This is here just as a check to see if our function works correctly
print(first_num * second_num)
