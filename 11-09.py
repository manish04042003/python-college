def fact(n):
    if(n==1):
        return 1 ;
    n1 = fact(n-1)
    temp = n * n1
    return temp 


ans = fact(10)
print(ans)
