"""OOPS"""
# class Student:
#     name="Rahul"
#     id=57
#     email="rs4655742@gmail.com"
# s1=Student()
# print(s1.id)

"""Constracter Parametarised"""
# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         print("Add new object in Data")

# s1=Student("Rahul",88)
# print(s1.name, s1.id)


"""Non parametarised"""
# class Student:
#     def __init__(self,id):        # nonn
#         pass

#     def __init__(self,name):
#         self.name=name
#         print("add new")
# s1=Student("Rahul")
# print(s1.name)



"""Practis Question 1"""
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"Your Average Is:",sum/3)

# s1=Student("Rahul",[50,50,80])
# s1.get_avg()



"""Practes Question 2"""
# class Acc :
#     def __init__(self,bal, acc):
#         self.balance=bal
#         self.account=acc

#     def debit (self,amount):
#         self.balance-=amount
#         print("Rs",amount,"Was Dabited")
#         print("Total Ballance is",self.get_b())

#     def credit (self,amount):
#         self.balance+=amount
#         print("Rs",amount,"Was Cradit")
#         print("Total Ballance is",self.get_b())

#     def get_b(self):
#         return self.balance


# acc1=Acc(1000,2000)
# acc1.credit(1000)
# acc1.credit(500)
# # print(acc1.balance)
# # print(acc1.account)



