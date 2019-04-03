
'''
定义一个学生类，用来形容学生
'''
'''
#定义一个空的类
class Student():
    #一个空类，pass代表直接跳过
    #此处pass必须有
    pass
mingyue = Student()

#再定义一个类，用来描述听Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    #需要注意
    #1.def doHoework的缩进层级
    #2.系统默认由一个self参数
    def doHomework(self):
        print("I 在做作业")
        #推荐在函数末尾使用return
        return None
#实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.doHomework()


class Teacher():
    name = "dana"
    age = 19

    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
        def sayAgain():
            print(__class__.name)
            print(__class__.age)
            print("Hello,nice to see you again")
t = Teacher()
t.say()
#Teacher.sayAgain()
'''

#继承语法
class Person():
    name = "NoName"
    age = 0

    def sleep(self):
        print("Sleeping......")
#父类写在括号内
class Teacher(Person):
    pass

t = Teacher()
print(t.name)
print(Teacher.name)

