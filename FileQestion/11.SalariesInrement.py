# Take input from user
salaries = list(map(float, input("Enter employee salaries separated by space: ").split()))

# New list to store updated salaries
updated_salaries = [] 

for sal in salaries:
    new_sal = sal + (sal * 0.10)   # increase salary by 10%
    updated_salaries.append(new_sal) 

print("Original Salaries:", salaries)
print("Updated Salaries:", updated_salaries)
