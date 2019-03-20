class Student():
    name = "dana"
    age = 18

#a=A._dict_
#print(a)

#yueyue = Student()
#print(yueyue.name)
#??say?????????selfself
def say(self):
    self.name = "aaaa"
    self.age = 200
    print("My name is {0}".format(self.name))
    print("My age is {0}".format(self.age))
yueyue = Student()
print(yueyue.say())