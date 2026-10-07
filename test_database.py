import database


database.create_table()


database.create_employee(
    "Rudrashis Chowdhury",
    "rudrashis.chowdhury@gmail.com",
    "AI & ML",
    60000,
    "Kolkata"
)


database.create_employee(
    "Tuhin Roy",
    "tuhinroy012@gmail.com",
    "Technology",
    15000,
    "Kolkata"
)


employees = database.get_all_employees()

print(employees)


print(
    database.search_by_department("IT")
)


print(
    database.search_by_city("Kolkata")
)


print(
    database.count_employees()
)


print(
    database.highest_salary()
)