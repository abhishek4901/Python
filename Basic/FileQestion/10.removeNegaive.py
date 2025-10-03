# Input: sales data
sales = list(map(int, input("Enter daily sales separated by space: ").split()))

# Remove negative values
cleaned_sales = []
for s in sales:
    if s >= 0:
        cleaned_sales.append(s)

print("Cleaned Sales Data:", cleaned_sales)
