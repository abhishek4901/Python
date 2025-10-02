# Take input from user
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

# First, check if lengths are equal
if len(str1) != len(str2):
    print("The strings are NOT anagrams.")
else:
    # Count characters in first string
    count1 = {}
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    # Count characters in second string
    count2 = {}
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    # Compare both dictionaries
    if count1 == count2:
        print("The strings are anagrams.")
    else:
        print("The strings are NOT anagrams.")
