"""Python List"""
# marks=[25.3,65.2,52.2,87.2]
# print(marks[3])

"""Index"""
# data=["Rahul",57,"Chitkara"]
# print(data[0])
# data[0]="Dustu"
# print(data[0])

"""Function"""
# num=[8,5,6,9,7,3]
# num.append(1)       #append
# list=num.sort()
# list=num.sort(reverse=True)
# print(list)
# print(num)


# list=["banana","rahul","apple"]
# list1=[5,6,8,9,]
# # print(list.sort(reverse=True))
# # list.reverse()
# # list.insert(1,"orange")
# # list1.insert(1,0)
# # list1.remove(9)
# list1.pop(1)
# print(list1)
# print(list)


"""TUPLE"""
# tup=(2,5,8,7,8)
# # print(type(tup))
# # print(tup[0])
# print(tup.index(2))
# print(tup.count(8))


"""movie question 1"""
# movie=[]
# mov1=input("Enter the first movie:")
# mov2=input("Enter the Secound movie:")
# mov3=input("Enter the Thard movie:")
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)

"""Palindr qs2 """
# list1=["m","a","a","m"]
# list2=[6,5,8]

# list_copy=list1.copy()
# list_copy.reverse()
# if(list_copy==list1):
#     print("This is Palindrom")
# else:
#     print("Not a Palindrom")



"""Count tuple QS3"""
# tup=("a","b","a","a")
# t=tup.count("a")
# print(t)


"""Asending order qs4"""
# str=["k","a","c","b","r"]      #list
# str.sort()
# print(type(str))








# Example of predefined Python functions

# 1. abs() - Get absolute value
print(abs(-10))  # Output: 10

# 2. len() - Get length of a list
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

# 3. sum() - Sum of elements in the list
print(sum(my_list))  # Output: 15

# 4. min() and max() - Get minimum and maximum values
print(min(my_list))  # Output: 1
print(max(my_list))  # Output: 5

# 5. sorted() - Return a sorted list
print(sorted(my_list, reverse=True))  # Output: [5, 4, 3, 2, 1]

# 6. type() - Check type of a variable
print(type(my_list))  # Output: <class 'list'>

# 7. round() - Round a floating point number
print(round(3.14159, 2))  # Output: 3.14

# 8. pow() - Power of a number
print(pow(2, 3))  # Output: 8

# 9. any() and all() - Check if any or all elements are true
print(any([0, 1, 0]))  # Output: True
print(all([1, 2, 3]))  # Output: True

# 10. zip() - Combine two lists element-wise
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# List example
my_array = [10, 20, 30, 40, 50, 60, 70, 80]

# 1. Basic slicing [start:end] - Slice elements from index 1 to 4 (end is exclusive)
slice1 = my_array[1:5]
print("Slice 1 (index 1 to 4):", slice1)  # Output: [20, 30, 40, 50]

# 2. Slicing with step [start:end:step] - Slice every second element from index 0 to 5
slice2 = my_array[0:6:2]
print("Slice 2 (every second element):", slice2)  # Output: [10, 30, 50]

# 3. Slicing from start to index - Slice elements up to index 3
slice3 = my_array[:4]
print("Slice 3 (up to index 3):", slice3)  # Output: [10, 20, 30, 40]

# 4. Slicing from index to end - Slice elements from index 3 to the end
slice4 = my_array[3:]
print("Slice 4 (from index 3 to end):", slice4)  # Output: [40, 50, 60, 70, 80]

# 5. Negative slicing - Slice elements from the end using negative indices
slice5 = my_array[-4:-1]
print("Slice 5 (negative indices):", slice5)  # Output: [50, 60, 70]

# 6. Reverse slicing - Reverse the list using slicing
reverse_slice = my_array[::-1]
print("Reversed array using slicing:", reverse_slice)  # Output: [80, 70, 60, 50, 40, 30, 20, 10]




# Sample string for demonstration
text = "  Hello World!  "

# 1. lower() - Converts all characters to lowercase
print(text.lower())  # Output: "  hello world!  "

# 2. upper() - Converts all characters to uppercase
print(text.upper())  # Output: "  HELLO WORLD!  "

# 3. strip() - Removes leading and trailing spaces
print(text.strip())  # Output: "Hello World!"

# 4. lstrip() - Removes leading spaces
print(text.lstrip())  # Output: "Hello World!  "

# 5. rstrip() - Removes trailing spaces
print(text.rstrip())  # Output: "  Hello World!"

# 6. replace() - Replaces a substring with another substring
print(text.replace("World", "Python"))  # Output: "  Hello Python!  "

# 7. split() - Splits the string into a list of substrings based on a delimiter (default: space)
print(text.split())  # Output: ['Hello', 'World!']

# 8. join() - Joins a list of strings into a single string, with a specified delimiter
words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: "Python is fun"

# 9. find() - Finds the index of the first occurrence of a substring
print(text.find("World"))  # Output: 8

# 10. count() - Counts the occurrences of a substring
print(text.count("l"))  # Output: 3

# 11. startswith() - Checks if the string starts with a specified substring
print(text.startswith("  Hello"))  # Output: True

# 12. endswith() - Checks if the string ends with a specified substring
print(text.endswith("!  "))  # Output: True

# 13. isalpha() - Checks if all characters in the string are alphabetic (ignores spaces)
print("Hello".isalpha())  # Output: True

# 14. isdigit() - Checks if all characters in the string are digits
print("12345".isdigit())  # Output: True

# 15. capitalize() - Capitalizes the first letter of the string
print(text.capitalize())  # Output: "  hello world!  "

# 16. title() - Capitalizes the first letter of each word
print(text.title())  # Output: "  Hello World!  "

# 17. swapcase() - Swaps case of all characters (lower to upper and vice versa)
print(text.swapcase())  # Output: "  hELLO wORLD!  "

# 18. index() - Finds the index of a substring (raises an error if not found)
print(text.index("World"))  # Output: 8

# 19. zfill() - Pads the string with leading zeros until it reaches the specified length
print("42".zfill(5))  # Output: "00042"
