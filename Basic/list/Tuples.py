b = (1,)#sigle value in tuple
c = () #empty tuple

a = ( 1,3,4,4,5,5,6,4,3,4)
print(type(a))#tuple
print(a)#(1, 3, 4, 4, 5, 5, 6, 4, 3, 4)
 #tuple function 
 
 #count() count the value 
a.count(4)
print(a)#(1, 3, 4, 4, 5, 5, 6, 4, 3, 4) because tuplle is immutable then exiting tuple value is not change
b = a.count(4)
print(b)#4 4 comes 4 time 