from generated_classes import Person, Employee

# Create instances of the generated classes
person = Person(name="Alice", age=30)
employee = Employee(name="Bob", age=40, employee_id="E123")

# Access their attributes
print(person.name, person.age)         # Output: Alice 30
print(employee.name, employee.age, employee.employee_id)  # Output: Bob 40 E123
