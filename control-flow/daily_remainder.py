task = input("Enter your task:")
time_bound = input("Is it time-bound:")
priority = input("Priority:")

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