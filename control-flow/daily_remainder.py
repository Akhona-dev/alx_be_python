task = input("Enter the Task description: ")
time_bound = input("Is the task Time Bound? (yes or no): ")
priority = input("Enter the task's Priority (high, medium, low): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)