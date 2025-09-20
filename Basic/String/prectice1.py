#print name and date 
letter = """   Dear <name>
your are selected
<date>"""
print(letter.replace("<name>","Abhishek").replace ("<date>", " 5 nov 2025"))

 #use find() to find double space 
a = "i am goood  boy" 
print(a.find(" "))#1  find single space  at index
print(a.find("  "))#10 find double space at index
print(a.find("   "))# if not found then return -1

#find the double space and use their single space 
a = "i am good   boy"
print(a.replace("   " , " "))# find s space and replace with single space
