s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Convert to lowercase
str1 = s1.lower().replace(" ", "")  
str2 = s2.lower().replace(" ", "") 

# Check if sorted strings are equal  
if sorted(str1) == sorted(str2):  
    print(f"'{s1}' and '{s2}' are anagrams")
else:
    print(f"'{s1}' and '{s2}' are not anagrams") 

 #usig frequency count 
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Convert to lowercase and remove spaces
str1 = s1.lower().replace(" ", "")
str2 = s2.lower().replace(" ", "")

# Quick check on length
if len(str1) != len(str2):
    print(f"'{s1}' and '{s2}' are not anagrams")
else:
    # Count frequency of characters in first string
    count1 = {}
    for c in str1:
        if c in count1:
            count1[c] += 1
        else:
            count1[c] = 1
    
    # Count frequency of characters in second string
    count2 = {}
    for c in str2:
        if c in count2:
            count2[c] += 1
        else:
            count2[c] = 1

    # Compare dictionaries
    if count1 == count2:
        print(f"'{s1}' and '{s2}' are anagrams")
    else:
        print(f"'{s1}' and '{s2}' are not anagrams")
