# # Input string
# s = input("Enter a string: ")
# rotations = []

# # Generate rotations
# for i in range(len(s)):
#     s = s[1:] + s[0]  # Move first character to the end
#     rotations.append(s)
# # Display rotations
# print(", ".join(rotations))
  
  
  #mauually
s = input("Enter a string: ")
n = len(s)

# Print rotations including original at the end
for i in range(1, n + 1):
    rotation = ""
    for j in range(0,n):
        rotation += s[(i + j) % n]
    print(f"{rotation}")

