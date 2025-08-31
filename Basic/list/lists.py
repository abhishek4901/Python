a = ["apple","raj" ,5, 4.5 ,"c"]
print(a)
print(a[0])#apple
print(a[3])#4.5
a[1] = "grapes" #but this is not possible in string, only happen in list(array)
print(a[1])#grapes

print(a[1:3])#['grapes', 5, 4.5]
print(a[1:4:2])#['grapes', 4.5]