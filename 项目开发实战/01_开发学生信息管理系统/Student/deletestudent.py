import student
import utils

def deleteStudent(filepath):
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
		
	instruct = input('确定删除? (Y/N):')
	if instruct.lower() == 'y':
		del studentList[idx] #删除找到的学生信息
	
		#接下来将已经删除掉指定学生信息的数据再次写入文件
		f = open(filepath, 'w')
		for stu in studentList:
			f.write(str(stu) + '\n')
		f.close()
		print('保存...')
