num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a Prime Number.")
else:
    flag = 0   # 0 means prime, 1 means not prime
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    
    if flag == 0:
        print(num, "is a Prime Number.")
    else:
        print(num, "is NOT a Prime Number.")
