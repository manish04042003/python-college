# ----------------------------------------if statements --------------------------------------
# if(True):
#     print("this statment is true");

# num = eval(input("Enter a number : "));
# if(num%5==0):
#     print('hiFive')



# ----------------------------------------if else statements --------------------------------------
# Odd even

# num = eval(input("Enter a number : "));
# if(num%2==0):
#     print('Even');
# else:
#     print('Odd');


# ---------------------------------------- nested if else statements --------------------------------------
# score = eval(input("enter the first number"))

# if(score>90):
#     print('F Grade');
# elif(score>80):
#     print('B Grade');
# elif(score>70):
#     print('C Grade');
# elif(score>60):
#     print('D Grade');
# else:
#     print('F Grade')
    

# ---------------------------------------- Loops --------------------------------------
# count = 0;
# while(count<10):
#       print("Programing is Fun");
#       count = count +1 ; 


# s= eval(input('Enter a number where you want to start the Sum : '))
# l= eval(input('Enter a number where you want to Sum : '))

# if(s>=l):
#     print("Enter a Valid Number")
# else:
#     sum = 0;
#     while(s<=l):
#         sum = sum + s;
#         s = s+1;
#     print("Sum is",sum)


#======================== Prime or Not 
# a = eval(input("enter the first number "));
# count = 2;
# while(count<a):
#     if(a%count==0):
#         print("not a Prime Number");
#         break;
#     count= count +1;
# else:
#     print("is a Prime Number");

# ===========================Twin prime

start = eval(input('Enter the strating number : '))
end = eval(input('Enter the Ending number : '))
lastPrime = 0;
count = 0 ;
while(start<=end):
    i = 2;
    while(i<start):
        if(start%i==0):
            break
        i=i+1;
    else:
        if(lastPrime ==(start-2)):
            count  = count + 1;
            print('(', end="");
            print(lastPrime,",",start ,end="");
            print(')', end="");
            print(',', end="");
        lastPrime = start ;
    start = start +1 ;

    


# for loop implimention

# sum =0 ;

# for i in range(0 ,11,1):
#     sum+=i;



# for i in range(11,1,-2):
#     sum +=i ;


# print(sum)


# checkr = eval(input('Enter a Number '));


# for i in range(2,checkr//2,1):
#     if(checkr % i == 0):
#         print('it is not a prime number')
#         break ;
# else:
#     print('yes it is a prime number')

# n= eval(input('Enter a Number : '))

# for i in range(1 , n+1):
#     if(i%2==0):
#         str = "*";
#     else:
#         str = "@";
#     for j in range(1,i+1):
#         print(str,end="")
#     print()
