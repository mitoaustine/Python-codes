class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def add_hours(self, hours):
        self.hours_worked += hours

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_payroll(self):
        for employee in self.employees:
            print(f"Pay {employee.name} ${employee.calculate_pay():.2f}")

# Example usage:
employee1 = Employee("Alice", 20)
employee1.add_hours(40)
employee2 = Employee("Bob", 25)
employee2.add_hours(35)

payroll_system = PayrollSystem()
payroll_system.add_employee(employee1)
payroll_system.add_employee(employee2)
payroll_system.process_payroll()