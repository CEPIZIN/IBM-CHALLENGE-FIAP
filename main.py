password = "548400"
data = []

def validate_password(correct_password):
    while True:
        print("PASSWORD")
        user_password = input("->")
        if user_password == correct_password:
            print("Access granted.")
            break
        else:
            print("Invalid password.")
            continue

def add_report():
    print("Add a report (start with the date of occurrence - DD/MM/YYYY):")
    date_occurred = input("Date: ")
    time_occurred = input("Time: ")
    report_content = input("Report: ")

    report = {
        "date": date_occurred,
        "time": time_occurred,
        "content": report_content,
    }

    data.append(report)
    print("Report added successfully.")

def view_reports():
    print("ALERT!")
    print("This section is for viewing only")
    if not data:
        print("No data registered")
    else:
        for i, report in enumerate(data, 1):
            print(f"{i}. Date: {report['date']} Time: {report['time']} - {report['content']}")

def exit_program():
    print("Exiting...")
    exit()

menu_options = {
    "1": add_report,
    "2": view_reports,
    "3": exit_program,
}

# To execute the menu choice
while True:
    print("\nSelect an option:")
    print("1 - Add reports of events")
    print("2 - View list of events")
    print("3 - Exit")

    choice = input("->")
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid option. Please type again.")