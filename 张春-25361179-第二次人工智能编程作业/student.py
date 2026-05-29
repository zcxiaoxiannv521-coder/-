# Student类用于保存单个学生的基本信息
# 后续查询、随机点名和生成准考证时都会使用这些数据
class Student:
    # 创建学生对象时，将学生的各项信息保存为对象属性
    def __init__(self, number, name, gender, class_id, student_id, college):
        self.number = number  # 名单中的序号
        self.name = name  # 学生姓名
        self.gender = gender  # 性别
        self.class_id = class_id  # 班级编号
        self.student_id = student_id  # 学号
        self.college = college  # 所属学院
    # 用于输出当前学生的完整信息
     # 在“查询学生信息”功能中调用
    def show_info(self):
        print("查询结果：")
        print(
            "序号：", self.number,
            "姓名：", self.name,
            "性别：", self.gender,
            "班级：", self.class_id,
            "学号：", self.student_id,
            "学院：", self.college
        )