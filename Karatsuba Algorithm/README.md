This is an implementation of the Karatsuba multiplication algorithm.

The basic concept is in x * y we can split both x and y in half
(for example if x = 1234 then a= 12 and b= 34) and we plug these into
(10**n)*ac + (10 ** (n/2))(ad + bc) + bd, with recursive calls on each
multiplication until we arrive at the base case where both x and y are
1 digit. 

This implementation is not a complete implementation, because 
we still use normal multiplication for multiplying constants such as (10**n)
