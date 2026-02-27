"""Read a file"""
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# data=f.readline()
# print(data)
# print(type(data))
# f.close()




"""Write a file"""
# # f=open("simple.txt","r+")
# # f=open("simple.txt","w+")
# f=open("simple.txt","a+")

# data=f.write("actsdfdfd")
# # print(data)
# f.close()



"""with syntex"""
# with open("simple.txt","w") as f:
#     data=f.write("rahl")


"""Deliting File"""
# import os
# os.remove("simple.txt")



"""Practice Question 1 create and print file acoding to the question"""

# with open("P1.txt","w") as f:
#     data=f.write("Hi everyone\nWe are larning file i\o \nUsing java\nI like programing in java")
#     print(data)



"""Practice Question 2 """
# with open("P1.txt","r") as f:
#     data=f.read()
# new=data.replace("java","python")
# print(new)

# with open("P1.txt","w") as f:
#     data=f.write(new)


"""Practice Question 3 """
# word="larning"
# with open("p1.txt","r") as f:
#     data=f.read()
#     if(data.find(word) != -1):
#         print("find")
#     else:
#         print("not found")


"""Practice Question 4 """
# def che():
#     word="xlarning"
#     with open("p1.txt","r") as f:
#         data=f.read()
#         if(word in data):
#             print("find")
#         else:
#             print("not found")

# def chec():
#     word = "I"
#     data=True
#     line=1
#     with open("p1.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line)
#                 return
#             line+=1
#     return -1

# chec()



"""Practice Question 4"""
count=0
with open("p1.txt","r") as f:
    data=f.read()
    
    num=data.split(",")
    for val in num:
        if((val) % 2 == 0):
            count += 1
print(count)


