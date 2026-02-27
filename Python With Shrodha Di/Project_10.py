"""Example to ganarate a randome number"""
# import random
# # r=random.randrange(15)
# r=random.randint(5,12)
# print(r)



"""Project 1 Gase a number"""
# import random
# target=random.randint(1,100)
# pas=random.choice(["d","r","k","o","l","f"])

# while True:
#     user=int(input("Gues The Targate"))
#     if(user==target):
#         print("Succesfull Gues")
#         break
#     elif(user<target):
#         print("Your Number Is to small.!! take a bigger")
#     else:
#         print("Your Number Is to Big.!! take a smaller")

# print("-------game over-------")





"""project 2 randome passward ganarate"""
# import random
# import string
# pass_len=12
# carValues=string.ascii_letters+string.digits+string.punctuation
# # print(string.ascii_letters)
# # print(string.digits)
# # print(string.punctuation)
# # print(random.choice(carValues))
# password=""
# for i in range(pass_len):
#     password +=random.choice(carValues)

# print("Your Randam Passward Is:",password)



"""project 3 randome passward ganarate Using List"""
import random
import string
pass_len=12
carValues=string.ascii_letters+string.digits+string.punctuation
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(random.choice(carValues))

res="".join([random.choice(carValues) for i in range(pass_len)])
print("Your Passward is:",res)


