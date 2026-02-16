class Employee:
    def __init__(self,name,designation,basic_salary):
        self.name=name
        self.designation=designation
        self.basic_salary=basic_salary
    def calculate_salary(self):
        if self.designation=="manager":
            a=0.30
        elif self.designation=="developer":
            a=0.20
        elif self.designation=="intern":
            a=0.10
        else:
            a=0.05
        final_salary=self.basic_salary+(self.basic_salary*a)
        return final_salary

name=input("Enter name: ")
designation=input("Enter designation(Manager/Developer/Intern): ").lower()
basic_salary=float(input("Enter basic salary: "))
emp=Employee(name,designation,basic_salary)

final=emp.calculate_salary()
print("\nEmployee Name: ",emp.name)
print("Designation:",emp.designation)
print("Final salary:",final)