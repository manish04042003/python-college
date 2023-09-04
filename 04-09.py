# mylist = []

# n = eval(input("Enter the length of the Array : "));

# for i in range(n):
#     print('Enter the Value of Index ',i ," :", end='') ;
#     a = eval(input())
#     mylist.append(a)

# print(mylist);

# power = []

# n = eval(input("Enter the length of the Array : "));

# for i in range(1,n):
#     # print('Enter the Value of Index ',i ," :", end='') ;
#     # a = eval(input())
#     power.append(2 ** i);

# print(power);

# ---------------------------------------Comprhension
power1 = [2 ** i for i in range(1,10) if i>5]
print(power1)