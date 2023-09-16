
def SumofDivisors(n):
    sum = 0 
    for i in range(1,n):
        if(n%i==0):
            sum = sum +i

    return sum

first = eval(input("Write a First Number : "))
last = eval(input("Write a Last Number : "))

if(first== SumofDivisors(last) and last == SumofDivisors(first)):
    print('yes')
else:
    print('No')