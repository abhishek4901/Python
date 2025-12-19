class Student:
    
    def getdata(self):
        self__name = input("enter  name :")
        self__rollno = int(input("enter roll no :"))  
    
     
    def show_data(self):
        print("\n--- Student Details ---")
        print(f"Name: {self__name}" "\t" roll no : {self__rollno})
        print(f"Roll Number: {self.roll_number}")
   
    def get__name(self):
        return self__name
    
    def get__rollno(self):
        return self_rollno

n = int(input("enter no of students"))
students = []


        
        for i in range(n):
            s = Student()
            s.getdata()
            students.append(s)

        # 3. Display all student details
        print("\nAll Student Details ")
        for idx, s in enumerate:
            s.show_data()

        # 4. Search loop
        while True:
            print("\nSearch options:")
            print(" 1 - Search by name (case-insensitive, partial match)")
            print(" 2 - Search by roll number (exact match)")
            print(" Exit  Quit search") 
            choice = input("Enter choice (1/2): ").strip().lower()

            if choice in ("q", "quit"):
                print("Exiting search.")
                break

            if choice == "1":
                key = input("Enter name to search: ").strip().lower()
                matches = [s for s in students if key in s.name.lower()]
                if matches:
                    print(f"\nFound {len(matches)} match(es):")
                    for m in matches:
                        m.show_data()
                else:
                    print("No student found with that name.")

            elif choice == "2":
                key = input("Enter roll number to search: ").strip()
                matches = [s for s in students if s.roll_number == key]
                if matches:
                    print(f"\nFound {len(matches)} match(es):")
                    for m in matches:
                        m.show_data()
                else:
                    print("No student found with that roll number.")

            else:
                print("Invalid choice. Enter 1, 2")
    
        final_choice = input("Do you want to run the program again (Y/N)? ").strip().lower()
        
        if final_choice not in ("y", "yes"):
            print("Thank you for using the Student Management System. Goodbye!")
            break 
