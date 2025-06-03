task = input("Enter your task:")
time_bound = input("Priority (high/medium/low):")
priority = input("Is it time-bound? (yes/no):")

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