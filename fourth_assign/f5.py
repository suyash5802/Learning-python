from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


# Subclass 1: Intern
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Subclass 2: Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, basic, bonus):
        self.basic = basic
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic + self.bonus


# Subclass 3: Contract Employee
class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
