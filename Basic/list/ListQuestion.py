import collections 

#Create the random 10  number  of the list
list1 = []
for i in range(4):
    num = int(input("Enter number :"  ))
    list1.append(num)
print(list1)

#display the list the maximun number of list
n = max(list1)
print(" maximum number in the list", n )




#display the list the smallest number of list
n = min(list1)
print(" minimum number in the list", n )

#sort item from the list 
n = sorted(list1)
print("sorted list :" ,n)


# display frequency of each number
frequency = collections.Counter(list1)
print("frequency :", frequency )

#remove the  dublicate 
n = list(set(list1))
print("remove the dublicates then list",n)



#display the list the maximun number of list without predefine function
for i in range(4):
    for j in range(4):
        if(list[i]>list[j+1]):
            list1[i]=list[j]
    print(list1)

