#display the list the maximun number of list without predefine function
list1 = [1,200,33]
for i in range(4):
    for j in range(4):
        if(list[i]>list[j+1]):
            list1[i]=list[j]
    print(list1)