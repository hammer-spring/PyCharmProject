import student

def searchStudentId(studentList, id):
	#查找需要操作的学生id
	idx = 0
	for stu in studentList:
		if stu.getStudentId() == id:
			return idx
		else:
			idx += 1
	return idx
	
def fileRead(filepath):
	#读入存储学生信息的文件，将所有学生信息读入内存
	f = open(filepath, 'r')
	studentList = []
	for line in f.readlines():
		stuInfo = line.strip().split()
		stu = student.Student(stuInfo[0], int(stuInfo[1]), int(stuInfo[2]))
		studentList.append(stu)
	f.close()
	return studentList
	
def fileWrite(filepath, studentList):
	#将存储学生信息的列表写入文件中
	f = open(filepath, 'w')
	for stu in studentList:
		f.write(str(stu) + '\n')
	f.close()
	
def checkId(id):
	#检查输入学号是否符合要求，这里假设学号为长度是4的数字
	#isdigit()方法检测字符串是否只由数字组成
	#如果字符串只包含数字则返回 True 否则返回 False。
	if len(id) == 4 and id.isdigit():
		return True
	else:
		return False
	
def checkGrade(grade):
	#检查输入成绩是否符合要求，这里假设成绩是0到100之间的整数
	if grade.isdigit() and int(grade) >= 0 and int(grade) < 101:
		return True
	else:
                return False
