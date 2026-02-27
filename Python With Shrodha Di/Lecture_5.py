"""Loop Statement"""
# count=1
# while count<=10:
#     print("RAHUL SAMANTA")
#     count += 1
# print(count)
    

"""Question 1:     1 to 100 print using loop"""
# i=1
# while i<=100:
#     print(i)
#     i += 1


"""Question 2  100 to 1 print using loop"""
# i=100
# while i>=1:
#     print(i)
#     i -= 1


"""Question 3  table of a perticuler number"""
# i=int(input("Enter a number:"))
# s=1
# while s<=10: 
#     print(i*s)
#     s += 1
    

"""Question 4  print """
# index=[1,4,9,16,25,36,49,64,81,100]
# ind=0
# while ind<len(index):
#     print(index[ind])
#     ind += 1


"""Question 5  find element """
# f=int(input("Enter a number:"))
# # f=3
# index=(1,2,3,6,8)
# i=0
# while i< len(index):
#     if(index[i]==f):
#         print("Fund")
#         # continue              #continue_for skip
#         break                   #break_for break the statement
#     i+=1
# print("End the loop")


"""Question 7  even print """
# i=1
# while i<=10:

#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i += 1




"""for loop"""

# num=[4,6,9,8,7,2]
# for i in num:
#     if(i==8):
#         print("8 is exis")
#         break
#     print(i)
# else:
#     print("End")
    


""" Question no 1 """
# ind=[1,4,9,16,25,36,49,64,81,100]
# for el in ind:
#     print(el)

""" Question no 1 """
# input1=int(input("Enter What is You are Search:"))
# Index=[1,4,9,16,25,36,49,64,81,100]
# input1=100

# for el in Index:
#     if(el==input1):
#         print("Element is finded:")



"""Range"""
# seq=range(5, 10)    #From to 
# for el in seq:
#     print(el)

# seq=range(8)          #stop
# for el in seq:
#     print(el)

# seq=range(5, 20, 3)
# for el in seq:
#     print(el)


"""Question odd even"""
# for i in range(1, 101, 2):
#     print(i)



"""Question 1 print number 1 to 100"""
# for el in range(1, 101):
#     print(el)


"""Question 2 print number 100 to 1"""
# for el in range(100, 0, -1):
#     print(el)

"""Question 3 print table of n number"""
# n=int(input("Enter:-"))
# for el in range(1, 11):
#     print(el*n)



"""Pass statement its basicaly use for try and catch"""
# for i in range(5):
#     pass
# if i>5:
#     pass
# print("Some Error This Code")


"""Practec question 1 sum of all"""
# n=7
# sum=0
# i=1

# while i<=n:
#     sum += i
#     i += 1
# print("Sum of two number is:",sum)




"""Practec question 2 factorial (While)"""
# n=5
# fact=1
# i=1

# while i<=n:
#     fact *= i
#     i += 1
# print("Sum of two number is:",fact)

"""Practec question 2 factorial (for)"""
# n=5
# factorial=1

# for i in range(1, n+1):
#     factorial *= i
# print("Factorial is:", factorial)
