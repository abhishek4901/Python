# Take input string
text = input("Enter a string: ")

# Dictionary to store frequency
freq = {}

# Count frequency of each character 
for char in text:
    if char in freq:
        freq[char] += 1 
    else:
        freq[char] = 1  

# Display result
print("Character Frequency:")
for key, value in freq.items():
    print(key, ":", value)
