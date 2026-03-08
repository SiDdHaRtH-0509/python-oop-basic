class Student:
    scholarship_cutoff = 7.0
    attendance_cutoff = 75

    def __init__(self, name, roll_no, branch, cgpa, attended, total):
        if total <= 0:
            raise  ValueError("Total classes must be greater than zero")

        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.cgpa = cgpa
        self.attended = attended
        self.total = total

    def attendance_percentage(self):
        return(self.attended/self.total)*100

    def check_scholarship(self):
        if self.cgpa >= self.scholarship_cutoff:
            print(f"{self.name} qualifies for scholarship")
        else:
            print(f"{self.name} does not qualify for the scholarship")

    def check_attendance(self):
        if self.attendance_percentage() >= self.attendance_cutoff:
            print(f"{self.name} meets the attendance requirement")
        else:
            print(f"{self.name} does not meet the attendance requirement")


    @classmethod
    def set_scholarship_cutoff(cls, new_cutoff):
        cls.scholarship_cutoff = new_cutoff

    @classmethod
    def set_attendance_cutoff(cls, new_cutoff):
        cls.attendance_cutoff = new_cutoff

s1 = Student("Max", 75, "Maths", 8.1, 89, 100)
s2 = Student("Josh", 91, "Commerce", 6.9, 58, 100)

Student.set_scholarship_cutoff(7.0)
Student.set_attendance_cutoff(75)

s1.check_scholarship()
s1.check_attendance()
s2.check_scholarship()
s2.check_attendance()