#scripts/core/handler/handler_student
from scripts.utility.mongodb import Mongodb
from scripts.schema import StudentDatabase


class StudentHandler:

    def __init__(self):
        self.student_obj = Mongodb()

    def add_new_student(self, stud: StudentDatabase):
        try:

            if self.student_obj.get_data_name(stud.name):
                return {"message": "student already exist"}
            self.student_obj.add_data(stud)
            return {"message": " new student added successfully"}
        except Exception as e:
            return {"Error": e}

    def view_all_data(self):
        try:
            if not self.student_obj.get_data():
                return {"message": "empty"}
            return self.student_obj.get_data()
        except Exception as e:
            return {"message": e}

    def del_student(self):
        try:
            if not self.student_obj.del_data():
                return {"message":"doesn't exist"}
            return self.student_obj.del_data()
        except Exception as e:
            return {"message": e}

    def cal_avg_age(self):
        try:
            return self.student_obj.aggregate()
        except Exception as e:
            return {"Error": e}


handler_obj = StudentHandler()