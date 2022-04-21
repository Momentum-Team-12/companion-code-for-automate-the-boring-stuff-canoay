print('How many hours did you work?')
hours_worked = float(input())
print('What is yout hourly rate?')
hourly_rate = float(input())
gross_pay = str(float(hours_worked * hourly_rate))

if hours_worked > 40:
    overtime = float(hours_worked - 40)
    overtime_pay = float(hourly_rate*1.5)
    total_overtime = float(overtime*overtime_pay)
