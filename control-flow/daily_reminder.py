task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority.")

if time_bound == "yes":
    print(" It requires immediate attention today!")