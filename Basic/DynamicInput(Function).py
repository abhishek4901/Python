class Student:
    def get_data(self):
        self.name = input("Enter student name: ")
        self.roll_number = input("Enter student roll number: ")

    def show_data(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

    def get_name(self):
        return self.name.lower()

    def get_roll_number(self):
        return self.roll_number


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
