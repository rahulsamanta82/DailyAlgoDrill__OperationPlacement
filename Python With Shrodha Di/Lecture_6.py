"""Function"""
# def fun1(a,b,c):
#     avg=(a+b+c)/3
#     # print(avg)
#     return avg
# avg=fun1(4,2,2)
# print(avg)



"""Default parameter"""
# def f(a,b=5):
#     sum=a*b
#     print(sum)
# f(2)



"""practes question 1 lenth of list"""
# city=["ghatal","daspur"]
# food=["chu","roll","maggi"]

# def de(lis):
#     print(len(lis))
# de(city)
# de(food)


"""practes question 2 print in one line """
# city=["ghatal","daspur"]
# def s(list):
#     for el in list:
#         print(el,end=" ")

# s(city)


"""practes question 3 factorial of n """
# def fact(a):
#     fa=1
#     for i in range(1, a+1):
#         fa *= i
#     print(fa)
# fact(5)


"""practes question 4 usd to inr """
# def con(usd):
#     inr=usd*82
#     print(usd,"usd=", inr,"inr")

# con(100)


"""practes question 5 home work"""
# def ch(a):
#     if(a%2==0):
#         print("even")
#     else:
#         print("odd")
# ch(2)


"""Recurtion"""
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)



"""Question prctic"""
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(5))


"""practic question 1 print use recurtion"""
# def sum(a):
#     if(a==0):
#         return 0
#     return sum(a-1)+a
#     # print(a)
#     # sum(a-1)
# print(sum(5))


"""practic question  print list use recurtion"""
# def prlist(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     prlist(list,idx+1)

# frout=["Apple","banana","liche","kala"]
# prlist(frout)
