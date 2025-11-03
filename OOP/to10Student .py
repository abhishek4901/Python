# ...existing code...
class Student:
    def _init_(self):
        self.name = ""
        self.roll_number = ""
        self.grade = ""

    def get_data(self):
        self.name = input("Enter student name: ").strip()
        self.roll_number = input("Enter student roll number: ").strip()
        self.grade = input("Enter student grade: ").strip()

    def show_data(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Grade: {self.grade}")


if _name_ == "_main_":
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    students = []
    for i in range(1, n + 1):
        print(f"\nEntering data for student {i}:")
        s = Student()
        s.get_data()
        students.append(s)

    print("\n=== All Student Details ===")
    for idx, s in enumerate(students, 1):
        print(f"\nStudent {idx}:")
        s.show_data()

    # Search menu: search by name or roll number
    while True:
        print("\nSearch options:")
        print("  1 - Search by name (case-insensitive, partial match)")
        print("  2 - Search by roll number (exact match)")
        print("  Q - Quit search")
        choice = input("Enter choice (1/2/Q): ").strip().lower()

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
            print("Invalid choice. Enter 1, 2 or Q.")

class Student:
    def _init_(self):
        self.name = ""
        self.roll_number = ""
        self.grade = ""

    def get_data(self):
        self.name = input("Enter student name: ").strip()
        self.roll_number = input("Enter student roll number: ").strip()
        self.grade = input("Enter student grade: ").strip()

    def show_data(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Grade: {self.grade}")


if _name_ == "_main_":
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    students = []
    for i in range(1, n + 1):
        print(f"\nEntering data for student {i}:")
        s = Student()
        s.get_data()
        students.append(s)

    print("\n=== All Student Details ===")
    for idx, s in enumerate(students, 1):
        print(f"\nStudent {idx}:")
        s.show_data()

    # Search menu: search by name or roll number
    while True:
        print("\nSearch options:")
        print("  1 - Search by name (case-insensitive, partial match)")
        print("  2 - Search by roll number (exact match)")
        print("  Q - Quit search")
        choice = input("Enter choice (1/2/Q): ").strip().lower()

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
            print("Invalid choice. Enter 1, 2 or Q.")
