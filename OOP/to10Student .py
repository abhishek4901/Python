class Student:
    def get_data(self):
        self.__name = input("Enter student name: ")
        self.__roll_number = input("Enter student roll number: ")

    def show_data(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.__name}")
        print(f"Roll Number: {self.__roll_number}")

    def get_name(self):
        return self.__name.lower()

    def get_roll_number(self):
        return self.__roll_number


# --- Main program ---
n = int(input("Enter number of students: "))
students = []

# Taking student data
for i in range(n):
    print(f"\nEntering data for student {i + 1}:")
    s = Student()
    s.get_data()
    students.append(s)

# Showing all data
print("\n=== All Student Details ===")
for i in range(n):
    print(f"\nStudent {i + 1}")
    students[i].show_data()

# Searching loop
while True:
    print("\nSearch options:")
    print("1 - Search by name (case-insensitive)")
    print("2 - Search by roll number")
    print("Q - Quit search")

    choice = input("Enter choice (1/2): ").lower()

    if choice == '1':
        name = input("Enter name to search: ").lower()
        found = False
        for s in students:
            if s.get_name() == name:
                print("\nStudent found:")
                s.show_data()
                found = True
        if not found:
            print("No student found with that name.")
    elif choice == '2' :
        roll_number = input("enter the roll  number to search ")
        found = False
        for s in students :
            if s.get_roll_number() == roll_number:
                 print("\nStudent found:")
            s.show_data()
            found = True
        if not found:
            print("No student found with that roll number.")

   

    cont = input("Do you want to continue? (yes/no): ").lower()
    if cont != 'yes':
        break
