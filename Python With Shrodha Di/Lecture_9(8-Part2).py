"""Delite Syntex"""
# class Student:
#     def __init__(self,name):
#         self.name=name

# s1 = Student("Rahul")
# print(s1.name)
# del s1.name           #delite object
# print(s1.name)


"""Public, Private,"""
# class Acc:
#     def __init__(self,Ac_no,Ac_pa):
#         self.Ac_no=Ac_no            #public
#         self.__Ac_pa=Ac_pa          #Private

#     def re_pa(self):
#         print(self.__Ac_pa)

# acc1=Acc("123","abc")
# print(acc1.Ac_no)
# # print(acc1.Ac_pa)
# print(acc1.re_pa())



"""Inharitance"""
# class car:
#     color="Black"
#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Stop The Car")

# class tyto(car):
#     def __init__(self,name):
#         self.name=name

# car1=tyto("Fortuner")
# car1=tyto("Marcides")
# print(car1.color)
# # print(car1.stop())




"""Class method"""
# class person:
#     name="animy"
#     def chname(self,name):
#         self.__class__.name="Rahul"
#         # self.name=name

# p1=person()
# p1.chname("Rahul")
# print(p1.name)










"""Polimorfizom overloading"""
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         newreal= self.real +num2.real
#         newimg= self.img +num2.img
#         return complex(newreal,newimg)


# num1=complex(2,4)
# num1.show()

# num2=complex(2,2)
# num2.show()

# # num3=num1.add(num2)
# num3=num1+num2
# print("--------")
# num3.show()






"""Practice question 1"""
class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, ord2):
        return self.price> ord2.price
    

ord1=order("Papse",40)
ord2=order("cock",30)

print(ord1>ord2)