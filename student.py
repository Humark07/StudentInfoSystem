class Student:
    def __init__(self, name, student_id, gender, classnum, college):
        # 初始化学生姓名、学号、性别、班级、学院等属性
        self.name = name
        self.student_id = student_id
        self.gender = gender
        self.classnum = classnum
        self.college = college

    def get_info(self):
        # 格式化输出信息，方便打印
        return f"姓名: {self.name} 性别: {self.gender} 班级: {self.classnum} 学号: {self.student_id} 学院: {self.college}"