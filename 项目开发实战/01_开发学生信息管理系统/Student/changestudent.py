import student
import utils

def changeStudent(filepath):
	f = open(filepath, 'r')
	#打开存储学生信息的文件，将所有学生信息读入内存
	studentList = [] #存储学生信息的列表
	for line in f.readlines():
		stuInfo = line.strip().split()
		stu = student.Student(stuInfo[0], int(stuInfo[1]), int(stuInfo[2]))
		studentList.append(stu)
	f.close()
	
	if len(studentList) == 0: #如果文件为空，退出当前操作
		print('没有学生信息! 请添加学生信息。')
		return
		
	id = input('请输入学生ID: ')
	idx = utils.searchStudentId(studentList, int(id))
	while idx >= len(studentList):
		id = input('学生信息没有找到, 请输入正确学生ID: ')
		idx = utils.searchStudentId(studentList, int(id))
		
	#简单起见，这里我们假设只能修改学生的分数，不能对姓名进行修改
	grade = input('请更改此学生的成绩: ')
	while not utils.checkGrade(grade):
		grade = input("格式错误! 请输入正确成绩: ")
		
	studentList[idx].setStudentGrade(grade)
	instruct = input('保存? (Y/N):')
	if instruct.lower() == 'y':
		f = open(filepath, 'w')
		for stu in studentList:
			f.write(str(stu) + '\n')
		f.close()
		print('保存...')
