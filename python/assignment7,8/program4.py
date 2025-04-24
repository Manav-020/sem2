class Employee:
    def __init__(self, name, salary):
        """
        Initialize an Employee object.

        Args:
            name (str): The employee's name.
            salary (float): The employee's salary.
        """
        self.name = name
        self.salary = salary

    def __add__(self, other):
        """
        Overload the + operator to combine two employees' salaries.

        Args:
            other (Employee): The other employee.

        Returns:
            float: The combined salary.
        """
        if isinstance(other, Employee):
            return self.salary + other.salary
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        """
        Overload the - operator to compare two employees' salaries.

        Args:
            other (Employee): The other employee.

        Returns:
            float: The difference in salaries.
        """
        if isinstance(other, Employee):
            return self.salary - other.salary
        else:
            raise TypeError("Unsupported operand type for -")

    def __str__(self):
        """
        Return a string representation of the Employee object.

        Returns:
            str: A string containing the employee's name and salary.
        """
        return f"{self.name} - Salary: {self.salary}"

# Example usage
emp1 = Employee("John Doe", 5000.0)
emp2 = Employee("Jane Doe", 6000.0)

print(emp1)  # Output: John Doe - Salary: 5000.0
print(emp2)  # Output: Jane Doe - Salary: 6000.0

combined_salary = emp1 + emp2
print("Combined Salary:", combined_salary)  # Output: Combined Salary: 11000.0

salary_difference = emp1 - emp2
print("Salary Difference:", salary_difference)  # Output: Salary Difference: -1000.0