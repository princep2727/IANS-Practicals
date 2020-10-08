def gcd(m,n):
    if m< n: 
        (m,n) = (n,m)
    while (m % n != 0):
        (m, n) = (n, m % n)
    return n

m=int(input("enter m value:"))
n=int(input("enter n value:"))
print("The GCD of the m and n is:")
print(gcd(m,n))
