class Student:
    def __init__(self, name, roll_no, branch, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.cgpa = cgpa
        
    def display(self):
        print("Name:-", self.name)
        print("Roll No:-", self.roll_no)
        print("Branch:-", self.branch)
        print("CGPA->", self.cgpa)

    def is_eligible(self):
        if self.cgpa >= 7.0:
            print("Eligible (CGPA ≥ 7.0)")
        else:
            print("Not Eligible (CGPA < 7.0)")


s1 = Student("Max", 75, "Maths", 8.1)
s2 = Student("Josh", 91, "Commerce", 6.9)

print("------")
s1.display()
s1.is_eligible()
s2.display()
s2.is_eligible()