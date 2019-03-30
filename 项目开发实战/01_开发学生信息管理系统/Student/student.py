class Student():
        def __init__(self, name, id, grade):
                '初始化函数'
                self.name = name
                self.id = id
                self.grade = grade
                
        def __lt__(self, other):
                '自定义比较器，这里使用student id来进行比较排序'
                return (self.grade > other.grade)
        def __str__(self):
                '将一个对象实例转换成一个字符串'
                return self.name + '\t' + str(self.id) + '\t' + str(self.grade)
        def getStudentName(self):
                return self.name
        
        def getStudentId(self):
                return self.id
        def getStudentGrade(self):
                return self.grade
        def setStudentGrade(self, grade):
                self.grade = grade
