class Student:
    
    def __init__(self):
        self.name = ""
        self.roll_number = ""
    
    def get_data(self):
        """Prompts the user to input student details."""
        self.name = input("Enter student name: ").strip()
        self.roll_number = input("Enter student roll number: ").strip()
     
    def show_data(self):
        """Prints the student's details."""
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
    

if __name__ == "__main__":
    
    # Outer loop to allow the entire program to run again
    while True: 
        
        # 1. Get number of students with validation
        while True:
            try:
                n = int(input("Enter number of students: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # 2. Collect student data
        students = []
        for i in range(1, n + 1):
            print(f"\nEntering data for student {i}:")
            s = Student()
            s.get_data()
            students.append(s)

        # 3. Display all student details
        print("\nAll Student Details ")
        for idx, s in enumerate(students, 1):
            print(f"\nStudent {idx}:")
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