# ===========================Twin prime

start = eval(input('Enter the strating number (>2) : '))

end = eval(input('Enter the Ending number : '))
lastPrime = 0;

while(start<=end):
    i = 2;
    while(i<start):
        if(start%i==0):
            break
        i=i+1;
    else:
        if(lastPrime ==(start-2)):
            print("(",lastPrime,",",start,")", end="");
        lastPrime = start ;
    start = start +1 ;
