class Student:

    def __init__(self, name, roll_no, branch, cgpa, subjects):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.cgpa = cgpa
        self.subjects = subjects

    # User-Presentation Print
    def __str__(self):
        return f"{self.name} ({self.branch}) | CGPA: {self.cgpa}"

    # Developer representation
    def __repr__(self):
        return f"Student({self.name}, {self.roll_no}, {self.branch}, {self.cgpa}, {self.subjects})"

    # Compare Students by CGPA
    def __lt__(self, other):
        return self.cgpa < other.cgpa

    # Compare Students by Roll.No
    def __eq__(self, other):
        return self.roll_no == other.roll_no

    # Combine Average CGPA of the class
    def __add__(self, other):
        return (self.cgpa + other.cgpa) / 2

    # Number of Subjects
    def __len__(self):
        return len(self.subjects)

class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if student in  self.students:
            print("Student with same roll number already exists.")
            return
        self.students.append(student)
        print(f"{student.name} added successfully.")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None

    def rank_students(self):
        return sorted(self.students, reverse=True)

    def average_cgpa(self):
        total = sum(student.cgpa for student in self.students)
        return total/len(self.students)

    def top_n_students(self, n):
        ranked = self.rank_students()
        return ranked[:n]

    def total_students(self):
        return len(self.students)

    def display_all(self):
        print("\n---: All Students :---")
        for student in self.students:
            print(student)


if __name__ == '__main__':

    sms = StudentManagementSystem()

    s1 = Student("Max", 75, "CSE", 8.7, ["Computer Networks", "Data Structures", "Operating Systems"])
    s2 = Student("Josh", 91, "Civil", 6.9, ["Surveying", "Structural Engineering", "Construction Management"])
    s3 = Student("Siddharth",19, "CSE",9.3, ["Python", "Cloud Computing", "Maths", "Algorithms", "Computer Architecture"])
    s4 = Student("Grace",25, "Accounting",7.49, ["Financial Accounting", "Cost Accounting", "Taxation", "Auditing"])
    s5 = Student("Nainsi",5, "MBA",9.5, ["Marketing Management", "Financial Management", "Business Strategy", "Operations Management", "Human Resource Management"])

    sms.add_student(s1)
    sms.add_student(s2)
    sms.add_student(s3)
    sms.add_student(s4)
    sms.add_student(s5)

    sms.display_all()

    print("\nTotal No of Student:", sms.total_students())

    print("\n---: Leaderboard :---")
    for rank, student in enumerate(sms.rank_students(), start=1):
        print(f"Rank {rank}: {student}")

    print("\nAverage CGPA of the Class:", round(sms.average_cgpa(), 2))

    print("\nTop 2 Student:")
    for student in sms.top_n_students(2):
        print(student)

    print("\nSubjects taken by Nainsi :", len(s5))
    print("Subjects taken by Siddharth :", len(s3))

    print("\nCombined CGPA of Nainsi and Siddharth :", s3 + s5)

    print("\nSearching Roll No: 52")
    found = sms.search_student(52)
    if found:
        print("Found:", found)
    else:
        print("Student with this roll no was not found")
