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
        print("CGPA:-", self.cgpa)

class ResearchStudent(Student):

    def __init__(self, name, roll_no, branch, cgpa, publications):
        super().__init__(name, roll_no, branch, cgpa)
        self.publications = publications

    def check_research_grant(self):
        if self.publications >= 1:
            print(f"{self.name} is ELIGIBLE for the research grant")
        else:
            print(f"{self.name} is NOT ELIGIBLE for the research grant")

    def display(self):
        super().display()
        print("Publications:-", self.publications)


s1 = Student("Max",75, "CSE",8.7)
s2 = Student("Josh",91, "Civil",6.9)
s3 = Student("Tanvi",45, "Mechanical",6.3)

rs1 = ResearchStudent("Siddharth",19, "CSE",9.3,3)
rs2 = ResearchStudent("Nainsi",5, "B.Com",9.5,5)
rs3  =ResearchStudent("Grace",25, "Accounting",7.49,0)

print("\n--: Regular Student :--")

print()
s1.display()
s1.check_scholarship()

print()
s2.display()
s2.check_scholarship()

print()
s3.display()
s3.check_scholarship()

print("\n--: Research Student :--")

print()
rs1.display()
rs1.check_scholarship()
rs1.check_research_grant()

print()
rs2.display()
rs2.check_scholarship()
rs2.check_research_grant()

print()
rs3.display()
rs3.check_scholarship()
rs3.check_research_grant()