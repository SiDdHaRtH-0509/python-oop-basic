class Student:
    scholarship_cutoff = 7.0

    def __init__(self, name, roll_no, branch, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.cgpa = cgpa

    def check_scholarship(self):
        if self.cgpa >= self.scholarship_cutoff:
            print(f"{self.name} qualifies for scholarship")
        else:
            print(f"{self.name} does not qualify for the scholarship")

    def display(self):
        print("Name:-", self.name)
        print("Roll No:-", self.roll_no)
        print("Branch:-", self.branch)
        print("CGPA->", self.cgpa)

s1 = Student("Max", 75, "Maths", 8.1)
s2 = Student("Josh", 91, "Commerce", 6.9)
 
s1.display()
s1.check_scholarship()
s2.display()
s2.check_scholarship()