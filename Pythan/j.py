# def fun(nums):
#     single = 0
#     double = 0
    
#     for num in nums:
#         if 0 <= num <= 9:
#             single += num
#         elif 10 <= num <= 99:
#             double += num
    
#     total_sum = sum(nums)
    
#     alice_single = single
#     bob_double = total_sum - single
    
#     alice_sum_double = double
#     bob_sum_single = total_sum - double
    
#     if alice_single > bob_double or alice_sum_double > bob_sum_single:
#         return True
    
#     return False

# nums = [1, 2, 3, 4, 5, 14]
# print(fun(nums))  




# str="Name: Rahul, Id: 2213986057"
# s=str.replace("Name", "Name1")
# print(s)

# n=str(input("Enter Name:=>"))
# s=len(n)
# print(s)

# n=str(input("Enter Name:=>"))
# s=n.count("a")
# print(s)

# n=[2,3,5] #list

# n.sort()
# print(n)


# n=int(input("Enter a number=>"))
# def fun(n):
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")

# fun(n)


str="rahulsamanta"
str1="DustuSamanta"
# print(str.endswith("ta"))
# print(str.capitalize())
# print(str.replace("a","g"))
# print(str.find("r"))
# print(str.index("s"))
# print(str.upper())
# print(str.count("a"))
# print(str,str1)
# inf={
#     "name":"rahul",
#     "sub":["java","py"],
#     "tuple":(1,5,4)
# }

# print(type(inf))
# print(inf["name"])
# inf["name"]="sourav"
# print(inf["name"])
# print(inf["tuple"])
# print(inf.values())
# print(inf.keys())

# loop
# count=1
# while count<=10:
#     print("rahul")
#     count+=1
# print(count)



# # Prompting the user for input
# user_input = int(input())
# number_list = []
# for i in range(user_input):
#   number_list.append(int(input()))
# # Printing the list of numbers
# print("List of numbers:", number_list)



# user_input=int(input("Enter Your loop Size=>"))
# number_list=[]
# for i in range(user_input):
#   number_list.append(int(input()))
# print("list of numbers:=>",number_list)  




"""avarage number"""
# a=int(input("Enter your name=>"))
# v=int(input("Enter your name=>"))
# b=int(input("Enter your name=>"))
# g=int(input("Enter your name=>"))
# h=(a+v+b+g)/4
# print("ave is=>",h)

# str = "Sunilsahoo"
# n=str[5].replace("s","@")
# print(str)
# a = {1,2,5,1,2,1,5,7,2}
# print(a)

# light=input("enter color=>")
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("strt")
# else:
#     print("wrong")

# n=int(input("enter a number"))
# u=n%7
# if(u==0):
#     print("devisible")
# else:
#     print("not")

"""even or odd"""
# n=int(input("enter a number"))
# if(n%2==0):
#     print("prime")
# else:
#     print("not prime")


def is_prime(number):
    if number <= 1:
        return False  
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  
    
    return True  
# Example usage
num = int(input("Enter a number to check if it's a prime: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

str="rah/sa"
# str='rahul samanta'
# print(type(str))
# print(str)