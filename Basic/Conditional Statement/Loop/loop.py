#pre check - for while , first check condition
#break - exit current block, return current function se bahr krte, return 1 or 0(zero /non zero) -- then  that value  os ke pass chla jata then show program excute successfully  ,
#  exit(0)/(1) -- exit that program  that is call exit status
#post check - do while , last check condition 

# import math.sqrt(n) # for square root

n = int(input("Enter the number to check prime or not: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    for j in range(2, n // 2 + 1):  # loop from 2 to n/2
        if n % j == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
