# Input temperatures for 7 days
temps = list(map(float, input("Enter temperatures for 7 days separated by space: ").split()))

# Calculate average temperature
total = 0
for t in temps:
    total += t
average = total / len(temps)

# Count days above average
count = 0
for t in temps:
    if t > average:
        count += 1

print("Average Temperature:", average)
print("Number of days above average:", count)
