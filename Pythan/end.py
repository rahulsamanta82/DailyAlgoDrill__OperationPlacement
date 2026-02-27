# factorial
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# a=5
# print(fact(a))


# def prime(a):
#     if a<=1:
#         return False
#     else:
#         for i in range(2,a):
#             if a%i==0:
#                 return False
#             return True
# print(prime(7))
# print(prime(2))


# l=["a","b","m"]
# f=2
# l.insert(f, "t")
# print(l)


# List = ["Ram", "Shaym", "Ravi", "Advin"]
# List.pop(2)
# print(List)

# marks_list = [70, 50, 100, 40, 60]
# new_list = [marks for marks in marks_list if marks >= 60]
# print(new_list)
# n=[40,54,69,58]
# h=[m for m in n if m>=60]
# print(h)


# def rec_property(len, wid):
#     area = len * wid
#     perimeter = 2*(len + wid)
#     return [area, perimeter] 

# length = 10
# width = 5
# print(rec_property(length, width))


# def pi(l,w):
#     a=l*w
#     p=2*(l+w)
#     return [a,p]

# length=2
# width=6
# print(pi(length,width))



fruit_prices = {
    'apple': 1.0,
    'banana': 0.5,
    'cherry': 20,
    'date': 3.0,
    'elderberry': 1.5
}
new_list = {
    fruit : price for fruit, price in fruit_prices.items() if price > 1
}
print(new_list)

frout={
    'a':5,
    'b':8
}
n={
    f : m for f,m in frout.items() if m > 1
}
print(n)