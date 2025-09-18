n = input("Enter a character: ")
ch = n[0]

match ch: #block banne liye :
    case 'a'|'A'|'e'|'E'|'i'|'I'|'o'|'O'|'u'|'U' :
        print("vowel")
    case _ :#default case like this
        print("Consonent")

   
