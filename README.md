# 胡文炫-25361091-第二次人工智能编程作业
仓库链接：https://github.com/Humark07/StudentInfoSystem
## 1. 任务拆解与 AI 协作策略
步骤一：我先将文档喂给AI，并让它梳理要做什么准备，例如GitHub仓库的设置，三个py文件各自需要实现什么内容
步骤二：在student.py中定义学生类，并定义一个格式化函数，方便后续输出；在main.py中实现启动系统过程
步骤三：让AI生成ExamSystem类的核心代码框架，再由我在exam_system中手动实现。
## 2. 核心 Prompt 迭代记录
初始Prompt “写个Python学生管理系统，能查学生、点名、排考场、打印准考证。”
AI生成缺陷： 缺少异常处理，没有考虑用户输入非数字字符。
优化后Prompt：“请为ExamSystem类的random_roll_call方法添加健壮的异常处理，如果用户输入非整数、负数或超过总人数，请友好提示并重新输入。”
## 3. Debug 与异常处理记录
报错类型：FileNotFoundError
现象：运行后提示找不到“人工智能编程语言学生名单.txt”。
解决过程：我发现必须由用户在项目根目录下自行创建该文件。我在 `ExamSystem.__init__` 中添加了 `try...except`，如果文件不存在，提示用户生成该文件并退出程序，避免程序崩溃。
## 4. 人工代码审查 (Code Review)
    def random_roll_call(self):  #随机点名函数
        while True:
            try:
                num=int(input("请输入要点名学生数量："))  #输入需要点名人数
                if num not in range(1,len(self.student)+1):  #如果人数不在1到总人数范围内，则判断为输入错误
                    print("点名输入错误，请重新输入")
                    continue
                break
            except ValueError:   #使用try ，except排除非数字输入
                print("请输入有效整数")
        selected=random.sample(self.student,num) #在self.student列表中不重复地随机抽取num个元素
        print("\n本次随机点名结果：")
        for idx, stu in enumerate(selected, 1): #枚举获取索引和元素
            print(f"{idx}. {stu.name} {stu.student_id}")
