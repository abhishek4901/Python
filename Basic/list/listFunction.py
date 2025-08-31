a = [ 1,2,7,5,3,12,34,21]
print(a)#[1, 2, 7, 5, 3, 12, 34, 21]
 
#sort
a.sort()
print(a.sort())#none so not use this type
print(a)#[1, 2, 3, 5, 7, 12, 21, 34]

#append = insert at the end 
print(a.append("Mahadev"))#non but next print add mahadev so not use this type
a.append("ram")
print(a)# [1, 2, 3, 5, 7, 12, 21, 34, 'Mahadev', 'ram']
 
#insert add value any place
a.insert(2, 3333333)
print(a)#[1, 2, 3333333, 3, 5, 7, 12, 21, 34, 'Mahadev', 'ram']

#remove()  remove only sigle value from list directly
a.remove(12)#12 remove
print(a)
#a.remove("ram" , 1) #error
a.remove("ram")
print(a)#[1, 2, 3333333, 3, 5, 7, 21, 34, 'Mahadev']

#pop() use to delete vale using index and return that value
a.pop(1)
print(a)#print updated list[1, 3333333, 3, 5, 7, 21, 34, 'Mahadev']

print(a.pop(1))#here is working but only print the value of poped 3333333