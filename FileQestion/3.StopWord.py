# List of stop words
stop_words = ["is", "the", "a", "an", "of", "in", "on", "and", "to", "for"]

# Take input
text = input("Enter a sentence: ")

# Remove stop words using a simple loop
result = "" 
for word in text.split():
    if word.lower() not in stop_words:
        result += word + " "

print("original String ",text)
print("Without Stop Words:", result.strip())
