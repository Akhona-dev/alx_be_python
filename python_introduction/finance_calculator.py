monthly_income = int(input('Enter your monthly income:'))
monthly_expenses = int(input('Enter your total monthly expenses:'))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("User saves",monthly_savings,"per month and saves up to",projected_savings,"a year with interest included")