# Input string from user
text = input("Enter a sentence: ").lower().replace(" ","")
words = text.split()

count = {}
# Count each word
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

# Display the counts
print("Word count:")
for key, value in count.items():
    print(key, ":", value)
