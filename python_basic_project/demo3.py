class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks_list.append(mark)
        else:
            raise ValueError("Marks should be between 0 and 100")

    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())


student = Student("Gayatri", 101)

for i in range(3):
    try:
        mark = float(input("Enter mark: "))
        student.add_mark(mark)
    except ValueError as e:
        print(e)

student.display_info()