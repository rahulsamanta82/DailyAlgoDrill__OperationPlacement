# a=14
# b=5
# c=4
# def fun(a,b,c):
#     if (a>b and a>c):
#         print("A is grater.")
#     elif(b>a and b>c):
#         print("B is grater.")
#     else:
#         print("C is grater.")

# fun(a,b,c)



# def fun(f):
#     return 5*(f-32)/9

# f=int(input("Enter a Furenhite=>"))
# print(f"{round(fun(f),2)} digree C")



# print("a")
# print("b", end="")
# print("c", end="")


# def patern(n):
#     if(n==0):
#         return
#     print("*" *n)
#     patern(n-1)
# patern(3)


def fun(n):
    f=n*2.54
    return f
print(f"cms is=>{fun(6)}")


def rem(l, word):
    for item in l:
        l.remove(word)
        return l
l=["Harry", "Rahul","Sourav"]
print(rem(l, "Sourav"))


def mul(n):
    for i in range(1,11):
        print(n*i)

mul(5)