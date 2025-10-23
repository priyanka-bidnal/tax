salary = float(input("Enter original salary: "))
bonus_added = salary * 1.10  # salary + 10%
print(f"Original Salary: {int(salary) if salary.is_integer() else salary}")
print(f"Bonus Added: {int(bonus_added) if bonus_added.is_integer() else bonus_added}")
