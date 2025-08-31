#print name and date 
letter = """ Dear <name>
your are selected
<date>"""
print(letter.replace("<name>","abhishek").replace ("<date>", " 5 nov 2025"))

 #use find() to find double space 
a = "i am goood  boy" 
print(a.find(" "))#single space 1
print(a.find("  "))#duble space 10
print(a.find("   "))# if not found then return -1

#find the double space and use their single space 
a = "i am good  boy"
print(a.replace("  " , " "))
