# """Directory"""
# info={
#     "Name":"Rahul",
#     "Cgpa":8.97,
#     "Subject":["Java","Python"],
#     "tuple":("Rahul","Sourav"),
#     57:60,
# }
# print(info)
# print(type(info))

# print(info["Name"])
# info["Name"]="Sourav"
# info["sarename"]="Teli"
# print(info)

"""Nested Dictinary"""
# dec={
#     "name":"rahul",
#     "Performance":
#     {

#         "java":89,
#         "Python":98
#     }
# }

# print(dec["Performance"])
# print(dec["Performance"]["java"])
# print(list(dec.values()))
# print((dec.values()))
# print((dec.keys()))
# print(dec.items())
# print(dec.get("name"))
# print(dec["name"])
# dec.update({"Id":57})
# print(dec)







"""SET & METHODES"""
# decc={4,8,9,"A","B","k"}
# print(type(decc))
# print(decc)     #unorder value print

# deec= set()         #create empty Set
# print(type(deec))
# deec.add(1)
# deec.add(2)
# deec.add(3)
# deec.remove(1)
# print(deec)
# deec.pop()
# print(deec)
# deec.clear()
# print(len(deec))

# set1={1,5,8,8}
# set2={7,5,2,3}
# print(set1.intersection(set2))
# print(set1.union(set2))




"""Questions 1"""
# dec={
#     "cat":"a small animal",
#     "table":["a piece of fortuner","list of factes and figur"],
#     "id":{
#         "name":"rahul"

#     }
# }
# print(dec)


"""Questions 2"""
# set1={"python","java","c++","python","javascript","java","python","java","c++","c"}
# retr=set1.intersection()
# ans=len(retr)
# print(ans)
# print(len(set1))              #sort proces


"""Questions 2"""
# marks={}
# a=int(input("Enter Math:"))
# marks.update({"math":a})

# b=int(input("Enter phy:"))
# marks.update({"phy":b})

# c=int(input("Enter chu:"))
# marks.update({"chu":c})

# print(marks)



"""Questions 2"""
data={9,9.25}
data={
    ("flote",8.02),
    ("int",12)


}
print(data)
