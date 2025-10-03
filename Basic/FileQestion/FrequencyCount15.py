# Input: list of product IDs sold
products = list(map(int, input("Enter product IDs sold separated by space: ").split()))

# Dictionary to count frequency
freq = {}
for p in products:
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1

# Find product ID with maximum frequency
most_sold = None
max_count = 0
for key, value in freq.items():
    if value > max_count:
        max_count = value
        most_sold = key

print(f"Most frequently sold product ID: {most_sold} (Sold {max_count} times)")
