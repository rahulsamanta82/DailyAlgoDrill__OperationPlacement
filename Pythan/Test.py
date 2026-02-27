# y=(input("Enter a first number "))
# i=(input("Enter a second number "))
# f=int(y)+int(i)
# print("Sun od y and i: "+str(f))



# a=int(input("inter"))
# b=int(input("input2"))
# print(a+b)



# x=float(input("Enter A Number"))
# print(x)
# print("type of name",type(x))


# print("Enter the value of a")
# a = int(input())
# print("Enter the value of b")
# b = int(input())
# c = a + b
# print("value of c is :", c)


# x,y = input().split()
# x = int(x)
# y = int(y)
# print((x+y))


# x,y=input().split()
# x=int(x)
# y=int(y)
# print((x*y))


                # practice question
# name=str(input("Enter your name=>"))
# print("My name is:=>",name)
# id=int(input("Enter your Id=>"))
# print("My ID is=>",id)



# Age=float(input("Enter your age=>"))
# if(Age>=18):
#     print("Congrates you are eligibale for vote")
# else:
#     print("Not for vote")



"""trafic light"""
# light=str(input("light:-"))
# if(light=="red"):
#     print("Stop the car.")
# elif(light=="green"):
#     print("Run the car.")
# elif(light=="yellow"):
#     print("Worning for slow")
# else:
#     print("Not a valid input")


"""simple interest"""
# p=float(input("enter principle=>"))
# t=float(input("enter time=>"))
# r=float(input("enter round=>"))
# si=(p*t*r)/100
# print("your answer is=>",si)


"""Area of a Square"""
# side=int(input("Enter your side"))
# area=side**2
# print("Area of Square is:=>",area)


"""average of three number"""
# n1=int(input("Enter first number =>"))
# n2=int(input("Enter sec number =>"))
# n3=int(input("Enter therd number =>"))
# avg=(n1+n2+n3)/3
# print("so,Average of three number is:",avg)


"""Grater then A and B"""
# a=int(input("Enter A value:"))
# b=int(input("Enter B value:"))
# if(a>b):
#     print("A is graterthen B")
# elif(a==b):
#     print("A Equel to B")
# else:
#     print("A is not graterthen or equel to b")


"""string"""
# str1="rah\nul"
# str2='rahul samanta'
# str3="""Dustu"""
# print(str3)


"""Concatination of string"""
str1="Rahul Samanta"
str2="Samanta"
# print(str1+str2)
# print(len(str2))
# print(str1[0])
# print(str1[-5:-1])

"""String Function"""
# s="Hi my name is rahul samanta"
# print(s.endswith("ta"))
# print(s.capitalize())  #first letter
# print(s.replace("Hi","Hello"))
# print(s.find("n"))
# print(s.count("n"))


"""Q1"""
# name=str(input("Enter your name=>"))
# print(len(name))

"""Q2"""
# name=input("Enter your name=>")
# print(name.count("$"))

"""Q3"""
# num=int(input("Enter your number=>"))
# n=num%2
# if (n==0):
#     print("Your number is even.")
# else:
#     print("This is odd number.")

"""Q4"""
# n1=int(input("enter first number=>"))
# n2=int(input("enter sec number=>"))
# n3=int(input("enter therd number=>"))
# if (n1>=n2 and n1>=n3):
#     print("first number is big.")
# elif(n2>=n3):
#     print("secound number is big.")
# else:
#     print("Therd number is big.")

"""Q5"""
# num=int(input("enter a number=>"))
# n=num%7
# if (n==0):
#     print("This number is devided by 7.")
# else:
#     print("Not devided by 7.")


"""Directory"""
# inf={
#     "name":"rahul",
#     "subject":["java","pythan"],
#     "cgpa":8.37,
#     "tuple":("rahul","soumen"),
#     57:22,
# }

# print(inf)
# print(type(inf))
# print(inf["name"])
# inf["name"]="sourav"
# inf["name"]="dustu"
# # print(inf["name"])
# inf["sarename"]="teli"

"""nested directory"""
# dec={
#     "name":"rahul",
#     "result":
#     {
#         "java":98,
#         "pythan":69,

#     }
# }

# print(dec["result"])
# print(dec["result"]["java"])
# print(list(dec.values()))
# print(dec.values())
# print(dec.keys())
# print(dec.items())
# print(dec.get("name"))
# print(dec["name"])
# print(dec["result"]["java"])
# dec.update({"id":57})
# print(dec.keys())
# print(dec.get("id"))
# print(dec)



"""set method"""
# de={4,5,9,"a","b","c"}
# print(de)
# print(type(de))

# dec=set()
# print(type(dec))
# dec.add(1)
# dec.add(2)
# print(dec)
# dec.remove(2)
# print(dec)
# dec.pop()
# print(dec)
# dec.clear()
# print(len(dec))

# set1={1,2,6,8}
# set2={6,7,1}
# print(set1.intersection(set2))
# print(set1.union(set2))



# dec={
#     "cat":"My Name is Rahul Samanta",
#     "About":["I love my moom","And Father Also"],
#     "id":{
#         "name":"Rahul"
#     }

# }
# print(dec)
# print(dec.keys())
# print(dec.values())
# print(dec["id"]["name"])



# marks={}
# print(type(marks))
# a=print(input("Enter Maths Number=>"))
# marks.update({"math":a})

# b=print(input("Enter Phy Number=>"))
# marks.update({"phy":b})

# c=print(input("Enter chu Number=>"))
# marks.update({"chumestry":c})
# print(marks)
# print(marks.values())

# data ={8,9,6}
# data={              #first priority
#     ("flote",8.36),
#     ("int",8)
# }
# print(data)

"""Loop Statement"""
# count=1
# while count<=10:
#     print("Rahul Samanta")
#     count+=1
# print(count)


# i=1
# while i<=100:
#     print(i)
#     i+=1


# i=100
# while i>=1:
#     print(i)
#     i-=1


# num=int(input("Enter A number=>"))
# n=1
# while n<=10:
#     print(num*n)
#     n+=1


# index=[1,2,23,65,7,8,9]
# ind=0
# while ind<len(index):
#     print(index[ind])
#     ind+=1


# ind=(1,5,83,7,2)
# find=int((input("Enter what is find you=>")))
# i=0
# while i<=len(ind):
#     if(ind[i]==find):
#         print("Yes Find it.")
#         break
#     i+=1
# print("End")


# i=0
# while i<=10:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# num=[5,9,7,3,8]
# for i in num:
#     if(i==8):
#         print("8 is find out in this index.")
#         break
#     # print(i)
# else:
#     print("not")
    
# ind=[4,6,2,7,1]
# for el in ind:
#     print(el)

# for i in range(10):          #fixed the range
#     print(i)



#start to end
# for i in range(5,10):
#     print(i)

# x=range(2,20,2)     #even
# for n in x:
#     print(n)

# for i in range(1, 20, 2):       #Odd number
#     print(i)

# for i in range(100, 0, -1):
#     print(i)


# n=int(input("Enter a number=>"))
# for i in range(1, 11):
#     print(n*i)


# for i in range(5):
#     pass
# if i>=5:
#     pass
# print("Some error this code.")



# n=int(input("Enter a number=>"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("Sum of two number is=>",sum)

# n=int(input("Enter a number=>"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("The sum of two number is",sum)


# n=4
# f=1
# i=1
# while i<=n:
#     f*=i
#     i+=1
# print("fatorian is=>",f)


# n=4
# f=1
# for i in range(1, n+1):
#     f*=i
# print("factorial of a number is using for loop.",f)

# n=4
# f=1
# for i in range(1, n+1):
#     f*=i
# print(f)
"""function"""
# def fun1(a,b,c):
#     avg=(a+b+c)/3
#     return avg
#     # print(avg)
# # fun1(2,2,2)
# avg=fun1(2,2,2)
# print(avg)

# def fun(a,b=5):
#     sum=a+b
#     print(sum)

# fun(2)


# city=["Ghatal","Daspur"]
# food=["Golga","Roll"]
# def fun(list,l):
#     print(list,l)
# fun(city,food)
# # fun(food)

# city=["ghatal","daspur"]
# def fun(list):
#     for el in list:
#         print(el,end="")
# fun(city)

# def fun(a):
#     fa=1
#     for i in range(1, a+1):
#         fa*=i
#     print(fa)
# fun(5)

# def fun(a):
#     fa=1
#     for i in range(1, a+1):
#         fa*=i
#     print(fa)
# fun(3)

# def con(usd):
#     inr=usd*82
#     print(usd,"usd=",inr)

# con(100)

# def fun(a):
#     if(a%2==0):
#         print("Even")
#     else:
#         print("Odd")
# fun(5)

"""recurtion"""
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fun(n):
#     if(n==10):  #base case
#         return
#     print(n)
#     fun(n+1)
# fun(1)


# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(3))

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(3))

# f=open("demo.txt","r")
# data=f.read()
# print(data)
# data=f.readline()
# print(data)
# print(type(data))
# f.close()






# inf={
#     "name":"Rahu",
#     "id":57,
#     "id":{
#         "name":"Rahul",
#         "id":58
#     }
# }

# print(inf.values())
# Python program to illustrate 
# chr() builtin function 


"""Char"""
# numbers = [97, 98, 128516] 
# print(type(numbers))

# for number in numbers: 
	
# 	# Convert ASCII-based number to character. 
# 	letter = chr(number) 
# 	print("Character of ASCII value", number, "is ", letter) 




# Python program to illustrate 
# chr() builtin function 
# numbers = [17, 38, 79] 

# for number in numbers: 
	
# 	# Convert ASCII-based number to character. 
# 	letter = chr(number) 
# 	print("Character of ASCII value", number, "is ", letter) 



"""scope variable"""
#locale
# def fun():
#     x=10
#     print(x)
# fun()

#enclosing
# def outer():
#     x=12
# def iner():
#     print("x")
# iner()
# outer()

# global
# x=15
# def fun():
#     print(x)
# fun()


# built in scope
# def fun():
#     print(len("rahulk"))
# fun()


# x=10
# y=3
# # v=x/y
# v=x//y
# print(v)

"""identical operator"""
# a = 10  
# b = 20
# c = a

# print(a is not b)  #True if the operands are identical
# print(a is b)       # True if the operands are not identical 



#Membership Operators
# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]

# if (x not in list):
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")

# if (y in list):
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")



# # Ternary Operator
# a, b = 10, 20
# max = b if a < b else a
# print(max)



# #switch
# def number_to_string(argument):
#     match argument:
#         case 0:
#             return "zero"
#         case 1:
#             return "one"
#         case 2:
#             return "two"
#         case default:
#             return "something"
 

# head = number_to_string(5)
# print(head)


# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
#         k=0
#         print()