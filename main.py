
from exam_system import ExamSystem
if __name__ == '__main__':
    try:
        system=ExamSystem()
        system.run()
    except Exception as e:
        print(f"系统出现未知错误: {e}")

