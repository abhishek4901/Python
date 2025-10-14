     #slicing()
   
s = input("enter the string ")
s_clean = s.lower()

if s_clean[::-1]:
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome") 
    
#Method 2: Using a loop
s = input("enter the string ")
s_clean = s.lower()
is_palindrome = True

for i in range(len(s_clean)//2):
    if s_clean[i] != s_clean[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")

