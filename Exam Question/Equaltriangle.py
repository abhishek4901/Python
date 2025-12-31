n =int(input("enter the num"))
for i in range(0, n+1):
    # print spaces
    for j in range(n - i):
        print(" ", end="")
    # print stars
    for k in range(0,i):
        print("*", end= " ")
    print()  # move to next line
   


n =int(input("enter the num"))
for i in range(1, n + 1):
    # print spaces first
    print(" " * (n - i), end="")
    
    # print numbers in sequence: 1 to (2*i - 1)
    for j in range(1, 2 * i):
        print("*", end="")
    
    print()  # move to next line