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


s= eval(input('Enter a number where you want to start the Sum : '))
l= eval(input('Enter a number where you want to Sum : '))

if(s>=l):
    print("Enter a Valid Number")
else:
    sum = 0;
    while(s<=l):
        sum = sum + s;
        s = s+1;
    print("Sum is",sum)

