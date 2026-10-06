# Student Grade Calculator
# Console based Python program (uses only the standard library)

# Five subjects, each out of 100 marks
subjects = [
    "Python",
    "Mathematics",
    "DBMS",
    "Web Technologies",
    "English"
]


# Function 1: calculate total marks
def calculate_total(marks):
    return sum(marks)


# Function 2: calculate percentage (has a default parameter)
def calculate_percentage(total, subjects, max_marks=100):
    return total / (subjects * max_marks) * 100


# Function 3: decide the grade from the percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# Function 4: PASS only when every subject is 40 or more
def get_result(marks, pass_mark=40):
    if all(m >= pass_mark for m in marks):
        return "PASS"
    else:
        return "FAIL"


# Read and validate the mark of one subject
def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Marks in {subject} (0-100): "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100")
            else:
                return mark
        except ValueError:
            print("Please enter a number")


def main():
    # Take the student name
    name = input("Enter student name: ")

    # Take marks for every subject using a for loop
    marks = []
    for subject in subjects:
        mark = get_mark(subject)
        marks.append(mark)

    # Calculate total, percentage, grade and result
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(subjects))
    grade = get_grade(percentage)
    result = get_result(marks)

    # Print the report card
    print()
    print("------ REPORT CARD ------")
    print(f"Student : {name}")

    # zip() pairs every subject with its mark
    for subject, mark in zip(subjects, marks):
        print(f"{subject:<18}: {mark:>5.1f}")

    print(f"{'Total':<18}: {total} / {len(subjects) * 100}")
    print(f"{'Percentage':<18}: {percentage:.2f}%")
    print(f"{'Grade':<18}: {grade}")
    print(f"{'Result':<18}: {result}")


if __name__ == "__main__":
    main()
