# 从exam_system模块中导入ExamSys类
from exam_system import ExamSys

if __name__ == "__main__":
    # 创建ExamSys对象并启动学生信息与考场管理系统
    system = ExamSys()
    system.run()