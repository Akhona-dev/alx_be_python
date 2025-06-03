task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

if priority == "high":
    print(f"Reminder: '{task}' is a HIGH priority task." + (" It requires immediate attention today!" if time_bound == "yes" else ""))
elif priority == "medium":
    print(f"Reminder: '{task}' is a MEDIUM priority task." + (" It requires immediate attention today!" if time_bound == "yes" else ""))
elif priority == "low":
    print(f"Reminder: '{task}' is a LOW priority task." + (" It requires immediate attention today!" if time_bound == "yes" else ""))
else:
    print(f"Reminder: '{task}' has an UNKNOWN priority." + (" It requires immediate attention today!" if time_bound == "yes" else ""))