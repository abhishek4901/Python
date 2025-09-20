#Reverse a string in python
#1. slicing
x = "hello"
x = x[::-1]#reverse the string including zero index, exclude zero index,and step -1
print(x)

# 2. using reversed() function
x = "hello"
x = ''.join(reversed(x))
print(x)

# 3. using loop
x = "hello"
y = "" #empty string
for i in x:
    y = i + y
print(y)


# 4. using stack
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str
s = "hello"
print(reverse_string(s))

# 5. using recursion
def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1]) 
s = "hello"
print(reverse_string_recursive(s))