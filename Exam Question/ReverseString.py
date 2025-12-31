#1️⃣ Using Indexing

#You can loop through the string from the end to the start using negative indexing:

s = input("enter the string ")
reversed_s = ""

# Loop from last index to first
for i in range(len(s)-1, -1, -1):
    reversed_s += s[i]

print(reversed_s)  # Output: nohtyP


#2️ Using Slicing

s = input("enter the  String ")
reversed_s = s[::-1]
print(reversed_s)  # Output: nohtyP


#recursion
def reverse_string(s):
    # Base case: if string is empty or single char
    if len(s) <= 1:
        return s
    # Recursive case: last char + reverse of rest
    return s[-1] + reverse_string(s[:-1])

s =input("enter the String ")
reversed_s = reverse_string(s)
print(reversed_s)  # Output: nohtyP
