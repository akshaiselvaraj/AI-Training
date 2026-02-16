class Student:
    def __init__(self,name,department,cgpa,year):
        self.name=name
        self.department=department
        self.cgpa=cgpa
        self.year=year
    def check_eligibility(self):
        if self.cgpa>=7.0 and self.year==4:
            return "Eligible for placement"
        else:
            return "Not eligible for placement"
        
name=input("Enter name:")
department=("Enter department:")
cgpa=float(input("Enter CGPA:"))
year=int(input("Enter year:"))    

student=Student(name,department,cgpa,year)
result=student.check_eligibility()
print("\nStudent Name:", student.name)
print("Department:", student.department)
print("Status:", result)