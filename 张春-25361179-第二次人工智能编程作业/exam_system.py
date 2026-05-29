import os
import random
from student import Student
# ExamSys类负责实现整个学生信息与考场管理系统的功能
class ExamSys:
    # 初始化系统，创建学生列表和考场安排列表
    # 程序启动时自动读取学生名单
    def __init__(self):
        self.students = []
        self.exam_arrangement = []
        self.load_students()
        # 从学生名单文件中读取学生信息
        # 将每一名学生的信息封装成Student对象并保存到列表中

    def load_students(self):
        file_names = [
            "人工智能编程语言学生名单.txt"
        ]

        file_path = None
        # 查找存在的学生名单文件
        for name in file_names:
            if os.path.exists(name):
                file_path = name
                break

        if file_path is None:
            print("未找到学生名单文件，请检查文件是否放在程序同一目录下。")
            return
        # 读取文件中的全部内容
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 第一行为表头，因此从第二行开始读取
        for line in lines[1:]:  # 跳过表头
            line = line.strip()
            # 跳过空行
            if line == "":
                continue

            parts = line.split()
            # 按照名单格式提取学生信息
            if len(parts) >= 6:
                number = parts[0]
                name = parts[1]
                gender = parts[2]
                class_id = parts[3]
                student_id = parts[4]
                college = parts[5]

                student = Student(number, name, gender, class_id, student_id, college)
                self.students.append(student)

        print("[系统] 已成功加载", len(self.students), "名学生信息。")

    # 系统主菜单，通过循环实现多个功能的调用
    def run(self):
        while True:
            print("===== 学生信息与考场管理系统 ===== \n"
                  "1. 查询学生信息 \n"
                  "2. 随机点名 \n"
                  "3. 生成考场安排表 \n"
                  "4. 生成准考证文件 \n"
                  "+--------------------------------------------------------------------------\n"
                  "0. 退出系统 ")
            choice=input("请输入功能编号：")
            # 限制输入范围，防止输入不存在的菜单编号
            while choice not in ["0", "1", "2", "3", "4"]:
                choice = input(
                    "功能编号不存在，请正确输入功能编号（0~4）："
                )
            if choice == "1":
                self.find_student()
            elif choice == "2":
                self.random_roll_call()
            elif choice == "3":
                self.generate_exam_arrangement()
            elif choice == "4":
                self.generate_admission_tickets()
            elif choice == "0":
                print("感谢使用，系统已退出。再见！")
                break

    # 根据学号查找学生信息
    # 如果找到则输出该学生的完整信息
    def find_student(self):
        student_id=input("请输入要查询的学号：")
        for student in self.students:
            if student.student_id == student_id:
                print("查询结果如下：")
                student.show_info()
                return

        print("未找到该学号对应的学生，请检查输入是否正确。")

    # 随机抽取指定数量的学生进行点名
    # 使用try-except处理各种非法输入情况
    def random_roll_call(self):

        total = len(self.students)

        while True:
            try:
                num = int(
                    input(f"请输入需要点名的学生数量（共 {total} 名学生）：")
                )
                # 点名人数不能超过总人数
                if num > total:
                    print(
                        f"[输入错误] 点名人数({num})超过学生总人数({total})，请重新输入。"
                    )
                    continue
                # 点名人数必须大于0
                if num <= 0:
                    print("[输入错误] 点名人数必须大于 0。")
                    continue
                # 使用sample实现不重复随机抽取
                selected_students = random.sample(self.students, num)

                print("\n本次随机点名结果：")

                for i, student in enumerate(selected_students, start=1):
                    print(
                        f"{i}.{student.name}    {student.student_id}"
                    )

                break


            except ValueError as e:

                print("[输入错误]", e)

    # 随机打乱学生顺序并生成考场安排表
    # 随机后的序号作为新的考场座位号
    def generate_exam_arrangement(self):
        self.exam_arrangement = self.students[:]
        # 打乱学生顺序
        random.shuffle(self.exam_arrangement)
        # 生成考场安排表文件
        with open("考场安排表.txt", "w", encoding="utf-8") as f:
            for i, student in enumerate(self.exam_arrangement, start=1):
                f.write(str(i) + "," + student.name + "," + student.student_id + "\n")

        print("考场安排表已生成：考场安排表.txt")

    # 根据考场安排信息生成准考证
    # 每位学生对应一个独立的txt文件
    def generate_admission_tickets(self):
        # 如果尚未生成考场安排表，则自动生成
        if len(self.exam_arrangement) == 0:
            self.generate_exam_arrangement()

        folder_name = "准考证"
        # 如果文件夹不存在则创建
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        for i, student in enumerate(self.exam_arrangement, start=1):
            # 生成01.txt、02.txt等文件名
            file_name = str(i).zfill(2) + ".txt"
            file_path = os.path.join(folder_name, file_name)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("考场座位号:" + str(i) + "\n")
                f.write("姓名:" + student.name + "\n")
                f.write("学号:" + student.student_id + "\n")

        print("准考证文件已生成，保存在【准考证】文件夹中。")
