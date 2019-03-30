import utils

def addStudent(filepath):
	print('请输入学生信息，其中ID为四位数字。')
	
	#输入新增学生信息：姓名，学号和成绩
	name = input("请输入学生姓名: ").replace(' ', '')
	id = input("请输入学生ID: ")
	while not utils.checkId(id):
		id = input("格式错误! 请输入正确ID格式: ")
	grade = input("请输入学生成绩: ")
	while not utils.checkGrade(grade):
		grade = input("格式错误! 请输入正确成绩格式: ")
	
	print('您已经成功添加:')
	print('姓名: ', name, ', ID: ', id, ', 成绩: ', grade)
	instruct = input('保存? (Y/N):')
	if instruct.lower() == 'y': #将输入信息统一转化为小写字母进行匹配
		f = open(filepath, 'a')
		#将学生信息写入文件，采用追加写方式
		#f.write('Name: ' + name + ', id: ' + id + ', grade: ' + grade + '\n')
		f.write(name + '\t' + id + '\t' + grade + '\n')
		f.close()
		print('保存...')
