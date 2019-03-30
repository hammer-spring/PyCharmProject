from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        """
        recognize start tag, like <div>
        :param tag:
        :param attrs:
        :return:
        """
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        """
        recognize end tag, like </div>
        :param tag:
        :return:
        """
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        """
        recognize data, html content string
        :param data:
        :return:
        """
        print("Encountered some data  :", data)

    def handle_startendtag(self, tag, attrs):
        """
        recognize tag that without endtag, like <img />
        :param tag:
        :param attrs:
        :return:
        """
        print("Encountered startendtag :", tag)

    def handle_comment(self,data):
        """

        :param data:
        :return:
        """
        print("Encountered comment :", data)

#打开HTML文件
path = "D:\\PyCharm\\PyCharmProject\\16_处理网页数据\\16.1 待解析的HTML文件.html"
filename = open(path)
data = filename.read()
filename.close()

#创建MyHTMLParser类的实例变量
p = MyHTMLParser()
p.feed(data)
p.close()
