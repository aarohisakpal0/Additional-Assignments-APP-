import csv
import argparse


def read_students(filename):
    """Read student records from a CSV file."""
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def display_students(students):
    """Display all student records."""
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 50)

    for student in students:
        print(
            f"Roll No: {student['Roll No']}, "
            f"Name: {student['Name']}, "
            f"Course: {student['Course']}, "
            f"Marks: {student['Marks']}"
        )


def search_student(students, roll_no):
    """Search for a student using Roll Number."""
    for student in students:
        if student["Roll No"] == roll_no:
            print("\nStudent Found")
            print("-" * 30)
            print(f"Roll No : {student['Roll No']}")
            print(f"Name    : {student['Name']}")
            print(f"Course  : {student['Course']}")
            print(f"Marks   : {student['Marks']}")
            return

    print("Student with this Roll Number was not found.")


def main():
    # Accept CSV filename from command line
    parser = argparse.ArgumentParser(
        description="Student Record Management System"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the student CSV file"
    )

    args = parser.parse_args()

    # Read student records
    students = read_students(args.file)

    # Display all records
    display_students(students)

    # Search for a student
    roll_no = input("\nEnter Roll Number to search: ")
    search_student(students, roll_no)


if __name__ == "__main__":
    main()