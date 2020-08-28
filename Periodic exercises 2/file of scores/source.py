class Grade:
    def __init__(self ,stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:

    def set_file(self, address):
        self.file = open(address,mode="a")
        self.lines = file.readlines()

    def load(self, line_number):
        if line_number > len(self.lines):
            return None
        info = self.lines[line_number - 1].split()
        grade = Grade(int(info[0]) ,int(info[1]) , float(info[2]))
        return grade


    