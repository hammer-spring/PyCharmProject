from html.parser import HTMLParser
class MyClass(HTMLParser):
    a_t=False
    def handle_starttag(self, tag, attrs):
        #print("开始一个标签:",tag)
        print()
        if str(tag).startswith("title"):
            print(tag)
            self.a_t=True
            for attr in attrs:
                print("   属性值：",attr)

    def handle_endtag(self, tag):
        if tag == "title":
            self.a_t=False
            #print("结束一个标签:",tag)

    def handle_data(self, data):
        if self.a_t is True:
            print("得到的数据: ",data)


#打开HTML文件
path = "D:\\PyCharm\\PyCharmProject\\16_处理网页数据\\16.7.html"
filename = open(path)
data = filename.read()
filename.close()

#创建myClass类的实例变量
p = MyClass()
p.feed(data)
p.close()
