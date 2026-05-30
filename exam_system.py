import os
import random

from student import Student
class ExamSystem:
    def __init__(self):
        self.student = []# 存储所有学生对象
        self.load_students()  # 初始化时加载学生数据

    def load_students(self):  #从文件中读取学生信息（支持制表符分隔，带表头
        filename="人工智能编程语言学生名单.txt"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    print("error!文件为空")
                    return
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue
                    parts= line.split('\t')
                    if len(parts)!=6:
                        continue
                    name=parts[1].strip()
                    gender=parts[2].strip()
                    classnum=parts[3].strip()
                    student_id=parts[4].strip()
                    college=parts[5].strip()
                    stu=Student(name,student_id,gender,classnum,college)
                    self.student.append(stu)
            print(f"已加载{len(self.student)}名学生信息")
        except FileNotFoundError:
            print("error!找不到文件")
            exit(1)

    def run(self):  #系统主菜单循环
        while True:
            menu = """
            ===== 学生信息与考场管理系统 =====
            1. 查询学生信息
            2. 随机点名
            3. 生成考场安排表
            4. 生成准考证文件
            --------------------------------
            0. 退出系统
            """
            print(menu)
            choice=input("请输入功能编号：").strip()
            if choice=="1":
                self.find_student()
            elif choice=="2":
                self.random_roll_call()
            elif choice=="3":
                self.generate_exam_arrangement()
            elif choice == '4':
                self.generate_admission_tickets()
            elif choice == '0':
                print("感谢使用，系统已退出。再见！")
                break
            else:
                print(f"功能编号不存在，请正确输入功能编号（0~4）：")

    def find_student(self):  #根据学号查询学生信息
        target_id=input("请输入要查询的学号:").strip()
        found=None
        for stu in self.student:
            if stu.student_id==target_id:
                found=stu
                break
        if found:
            print("\n查询结果：")
            print(f"序号: {self.student.index(found) + 1}  {found.get_info()}")
        else:
            print(f"未找到该学号对应的学生，请检查输入是否正确。")

    def random_roll_call(self):
        while True:
            try:
                num=int(input("请输入要点名学生数量："))
                if num not in range(1,len(self.student)+1):
                    print("点名输入错误，请重新输入")
                    continue
                break
            except ValueError:
                print("请输入有效整数")
        selected=random.sample(self.student,num)
        print("\n本次随机点名结果：")
        for idx, stu in enumerate(selected, 1):
            print(f"{idx}. {stu.name} {stu.student_id}")

    def generate_exam_arrangement(self): #生成考场安排表（随机打乱顺序）
        if not self.student:
            print("无学生数据，无法生成考场安排。")
            return
        shuffled = self.student[:]  # 复制列表
        random.shuffle(shuffled)  # 随机打乱
        output_file = "考场安排表.txt"
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                for idx, stu in enumerate(shuffled, 1):
                    f.write(f"{idx},{stu.name},{stu.student_id}\n")
            print("已生成完毕")
        except Exception as e:
            print(f"生成失败:{e}")

    def generate_admission_tickets(self):#生成准考证文件夹（基于已打乱的顺序）
        if not self.student:
            print("无学生数据，无法生成准考证。")
            return
        shuffled = self.student[:]
        random.shuffle(shuffled)
        folder = "准考证"
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
            for idx, stu in enumerate(shuffled, 1):
                filename = f"{idx:02d}.txt"
                filepath = os.path.join(folder, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"考场座位号:{idx}\n")
                    f.write(f"姓名:{stu.name}\n")
                    f.write(f"学号:{stu.student_id}\n")
            print(f"准考证已生成至文件夹:{folder}")
        except Exception as e:
            print(f"生成准考证失败:{e}")



