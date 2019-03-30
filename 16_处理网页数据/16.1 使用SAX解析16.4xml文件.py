import xml.sax

class bookHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.author = ""
      self.year = ""
      self.price = ""
      self.description = ""

   # 元素开始调用
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "book":
         print ("*****book*****")
         title = attributes["title"]
         print ("Title:", title)

   # 元素结束调用
   def endElement(self, tag):
      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "author":
         print ("author:", self.author)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "price":
         print ("price:", self.price)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # 读取字符时调用
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "author":
         self.author = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "price":
         self.price = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # 重写 ContextHandler
   Handler = bookHandler()
   parser.setContentHandler(Handler)
   
   parser.parse("D:\\PyCharm\\PyCharmProject\\16_处理网页数据\\16.4 待解析的XML文件.xml")
