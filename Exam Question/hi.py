# import sys
# a =10
# # print(sys.getsize(int))
# print(type([]))#class type list
# print(id(int))# address of a
# print(sys.getsizeof(a))#size of a 24int +4
s = "Hello"
# s[0] = "h"  ❌ Error, cannot change string characters

# Correct way to "change" string:
# s2 = "h" + s[3:]  # Create a new string
# print(s2)         # hello

numbers = [1, 2, 3,4,5,7]
# numbers.append(4)        # Add 4 at the end → [1,2,3,4]
# numbers.insert(1, 5)     # Insert 5 at index 1 → [1,5,2,3,4]
# numbers.remove(7)        # Remove 2 → [1,5,3,4]
# print(numbers)
def greet(name="User"):
    print("Hello", name)#Hello Amit

greet()#no  value pass then take default  value
greet("Amit")

