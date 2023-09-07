# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def multiplication_or_sum(n1,n2):
    if n1 * n2 <=1000:
        return(n1*n2)
    else:
        return(n1+n2)

print(multiplication_or_sum(20,30))
print(multiplication_or_sum(40,30))
