# """Predefine Array and list"""
# list=[1,2,3,4,5]
# print(abs(-10))
# print(len(list))
# print(sum(list))
# print(min(list))
# print(max(list))
# print(sorted(list,reverse=True))
# print(round(3.14159, 3))
# print(pow(2, 3))
# print(any([5, 1, 0]))  # Output: True
# print(all([1, 2, 3]))  # Output: True
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print(list(zip(list1, list2)))


# """Slicing"""
# my_array = [10, 20, 30, 40, 50, 60, 70, 80]
# slice1 = my_array[1:5]
# print("Slice 1 (index 1 to 4):", slice1)
# slice2 = my_array[0:6:2]
# print("Slice 2 (every second element):", slice2)
# slice3 = my_array[:4]
# print("Slice 3 (up to index 3):", slice3)
# slice4 = my_array[3:]
# print("Slice 4 (from index 3 to end):", slice4)  # Output: [40, 50, 60, 70, 80]
# slice5 = my_array[-4:-1]
# print("Slice 5 (negative indices):", slice5)
# reverse_slice = my_array[::-1]
# print("Reversed array using slicing:", reverse_slice)



# """String"""
text = "  Hello World!  "
print(text.lower())  # Output: "  hello world!  "
print(text.upper())
print(text.strip())
print(text.replace("World", "Python"))
print(text.split())
print(text.find("World"))
print(text.count("l"))


# """Dictinary"""
# inf={
#     "name":"rahul",
#     "id":57,
#     "tuple":[54,24],
#     "my":{
#         "java":50,
#         "c":28
#     }

# }

# print(inf["tuple"])
# print(type(inf))
# print(inf)
# inf["name"]="sourav"
# print(inf["name"])
# print(inf["my"]["java"])
# print(tuple(inf.get("name")))



# sub={
#     "a":60,
#     "b":65,
#     "c":40
# }

# avg=sum(sub.values())/len(sub)
# for subject, score in sub.items():
#     if score>avg:
#         print(subject)


# def find_duplicates(s):
#     return tuple(char for char in set (s) if s.count(char) > 1)
# input_string = "programming"
# duplicates = find_duplicates(input_string)
# print(f"Duplicate characters: {duplicates}")
# # return tuple(char for char in set(s) if s.(count(char)>1))




# # Define a tuple
# my_tuple = (10, 20, 30, 40, 50)

# # Element to search for
# element_to_search = 30

# # Searching for the element
# if element_to_search in my_tuple:
#     print(f"{element_to_search} is found in the tuple.")
# else:
#     print(f"{element_to_search} is not found in the tuple.")



# """sum of posative number"""

# import tkinter as tk
# from time import strftime


# def light_theme():
#     frame = tk.Frame(root, bg="white")
#     frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
#     lbl_1 = tk.Label(frame, font=('calibri', 40, 'bold'),
#                      background='White', foreground='black')
#     lbl_1.pack(anchor="s")

#     def time():
#         string = strftime('%I:%M:%S %p')
#         lbl_1.config(text=string)
#         lbl_1.after(1000, time)
#     time()


# def dark_theme():
#     frame = tk.Frame(root, bg="#22478a")
#     frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
#     lbl_2 = tk.Label(frame, font=('calibri', 40, 'bold'),
#                      background='#22478a', foreground='black')
#     lbl_2.pack(anchor="s")

#     def time():
#         string = strftime('%I:%M:%S %p')
#         lbl_2.config(text=string)
#         lbl_2.after(1000, time)
#     time()


# root = tk.Tk()
# root.title("Digital-Clock")
# canvas = tk.Canvas(root, height=140, width=400)
# canvas.pack()

# frame = tk.Frame(root, bg='#22478a')
# frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
# lbl = tk.Label(frame, font=('calibri', 40, 'bold'),
#                      background='#22478a', foreground='black')
# lbl.pack(anchor="s")

# def time():
#     string = strftime('%I:%M:%S %p')
#     lbl.config(text=string)
#     lbl.after(1000, time)
# time( )

# menubar = tk.Menu(root)
# theme_menu = tk.Menu(menubar, tearoff=0)
# theme_menu.add_command(label="Light", command=light_theme)
# theme_menu.add_command(label="Dark", command=dark_theme)
# menubar.add_cascade(label="Theme", menu=theme_menu)
# root.config(menu=menubar)
# root.mainloop()





text = "Hello World"
vowels = "aeiouAEIOU"
v_count = sum(1 for char in text if char in vowels)
c_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"Vowels: {v_count}, Consonants: {c_count}")


txt= "hello world"
vow="aeiouAEIOU"
VA_COUNT=sum(1 for char in txt if char in vowels)
cc_count=sum(1 for char in txt if char.isalpha() and char not in vow)
print(f"shhfhd {VA_COUNT} hbfedbdf {cc_count}")