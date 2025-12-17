def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining 🌟"
    elif marks >= 75:
        return "B", "Great job! You're doing very well 👍"
    elif marks >= 60:
        return "C", "Good effort! You can do even better 💪"
    elif marks >= 40:
        return "D", "Don't give up! Keep practicing 😊"
    else:
        return "F", "Stay positive! Hard work brings success 🚀"


while True:
    name = input("\nEnter student name: ")

    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print(" Marks must be between 0 and 100.")
        except ValueError:
            print(" Please enter a valid number.")

    grade, message = calculate_grade(marks)

    print("\n--- Result ---")
    print(f"Name   : {name}")
    print(f"Marks  : {marks}")
    print(f"Grade  : {grade}")
    print(f"Message: {message}")

    choice = input("\nAdd another student? (yes/no): ").lower()
    if choice != "yes":
        print("\n Program Ended")
        break
