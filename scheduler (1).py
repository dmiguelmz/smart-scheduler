exams = []  
def display_menu():
    print("\nSMART SCHEDULER ")
    print("1. Add a new exam")
    print("2. View all exams")
    print("3. Edit an exam")
    print("4. Delete an exam")
    print("5. Exit")

def add_exam():
    print("\n *Add New Exam*")
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter assigned room: ")

    new_exam = dict.fromkeys(['name', 'date', 'time', 'room'])
    new_exam.update({'name': name, 'date': date, 'time': time, 'room': room})

    exams.append(new_exam)
    print(f"Exam '{name}' added successfully!")

def view_exams():
    print("\n* All Scheduled Exams *")
    if not exams:
        print("No exams scheduled yet.")
        return
    for index, exam in enumerate(exams, start=1):
        print(f"\nExam #{index}")
        for key, value in exam.items():
            print(f"{key.capitalize()}: {value}")

def edit_exam():
    view_exams()
    if not exams:
        return
    try:
        index = int(input("\nEnter the exam number to edit: ")) - 1
        if 0 <= index < len(exams):
            exam = exams[index].copy()

            name = input(f"New name (current: {exam.get('name')}): ") or exam.get('name')
            date = input(f"New date (current: {exam.get('date')}): ") or exam.get('date')
            time = input(f"New time (current: {exam.get('time')}): ") or exam.get('time')
            room = input(f"New room (current: {exam.get('room')}): ") or exam.get('room')

            exams[index].update({'name': name, 'date': date, 'time': time, 'room': room})
            print("Exam updated successfully!")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_exam():
    view_exams()
    if not exams:
        return
    try:
        index = int(input("\nEnter the exam number to delete: ")) - 1
        if 0 <= index < len(exams):
            deleted = exams.pop(index)
            print(f" Exam '{deleted.get('name')}' deleted.")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Welcome to Smart Scheduler!")
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Thank you for using Smart Scheduler. ")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()

