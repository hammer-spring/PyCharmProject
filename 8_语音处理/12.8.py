import aifc

#创建一个新语音文件
stream = aifc.open("d:\\test.aifc", "w")
#声道数为2
stream.setnchannels(2)
#样本宽度为2
stream.setsampwidth(2)
#每一秒22050个帧
stream.setframerate(22050)
#写入表头以及语音串流
stream.writeframes(b"123456787654321" * 20000)
#关闭文件
stream.close()
