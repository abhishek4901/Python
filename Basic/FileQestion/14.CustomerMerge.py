# Input customer IDs for two branches
branch1 = list(map(int, input("Enter customer IDs for branch 1 separated by space: ").split()))
branch2 = list(map(int, input("Enter customer IDs for branch 2 separated by space: ").split()))

# Merge the two lists
all_customers = branch1 + branch2

# Remove duplicates using a set
unique_customers = list(set(all_customers))

# Sort in ascending order
unique_customers.sort()

print("Combined Customer IDs in Ascending Order:", unique_customers)
