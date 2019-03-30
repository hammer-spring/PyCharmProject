import student

def rankStudent(filepath):
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
	
	#方法1：使用lambda表达式给学生排序，按照学生成绩由高到底进行排序
	sortedStudentList = sorted(studentList, key=lambda stut: stut.getStudentGrade(), reverse=True)
	
	#方法2：在Student类中，我们自定义了内建的比较函数__lt__，所以可以直接对Student类的实例进行比较
	#sortedStudentList = sorted(studentList)
	print('姓名\tID\t成绩')
	for stu in sortedStudentList:
		print(stu.getStudentName() + '\t' + str(stu.getStudentId()) + '\t' + str(stu.getStudentGrade()))
