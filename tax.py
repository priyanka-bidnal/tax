salary = float(input("Enter original salary: "))
bonus_added = salary * 1.10  # after 10% bonus
after_tax = bonus_added * 0.95  # deduct 5% tax

print(f"Original Salary: {int(salary) if salary.is_integer() else salary}")
print(f"Bonus Added: {int(bonus_added) if bonus_added.is_integer() else bonus_added}")
print(f"After Tax Deduction: {int(after_tax) if after_tax.is_integer() else after_tax}")