import pandas as pd
data = {
    "Name": ["Amit", "Ravi", "Neha"],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)
print(df)
#   Name  Marks
#0  Amit     85
#1  Ravi     90
#2  Neha     88

# Accessing a column
print(df['Name'])
#0    Amit
#1    Ravi
#2    Neha

# Accessing a row by label
print(df.loc[0])
#Name: Name, dtype: object
#Name     Amit
#Marks      85

# Accessing an individual element
print(df.at[0, 'Name'])
#Name: 0, dtype: object
#Amit
