from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def salary(self):
        return 50000

class FullTimeEmployee(Employee):
    def salary(self):
        return 120000

