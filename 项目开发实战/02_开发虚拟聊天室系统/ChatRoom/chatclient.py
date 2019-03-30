#!/usr/bin/python  
# -*- coding: utf-8 -*-

import socket, select, threading, sys

class ChatClient():
	"""聊天室客户端类
	用以实现客户端的功能
	包括创建服客户端socket,连接服务器,收发服务器端和其他客户端的数据
	"""
	def __init__(self, host, port):
		self.HOST = host
		self.PORT = port
		self.client_socket = socket.socket()
		self.client_socket.connect((self.HOST, self.PORT))
		self.client_readlist = [self.client_socket]
	
	def receivemessage(self):		
		while True:
			readlist, writelist, errorlist = select.select(self.client_readlist, [], [])
			if self.client_socket in readlist:
				try:
					# 从服务器接收数据,数据buffer为4096
					print(self.client_socket.recv(4096).decode('utf-8'))
				except socket.error as err:
					print('连接错误...')
					exit()
		
	
	def sendmessage(self):
		# 发送数据,将客户端用户输入的信息发送出去
		while True:
			try:
				data = input()
			except Exception as e:
				print('对不起, 因为连接错误暂时无法输入信息。')
				#exit()
				break
			try:
				self.client_socket.send(data.encode('utf-8'))
			except Exception as e:
				exit()


	def run(self):
		# 分别启动接收数据和发送数据线程
		thread_recievemsg = threading.Thread(target=self.receivemessage)
		thread_recievemsg.start()
		
		thread_sendmsg = threading.Thread(target=self.sendmessage)
		thread_sendmsg.start()


if __name__ == "__main__":
	# 为了便于测试，这里使用本机hostname
	HOST = socket.gethostname()
	PORT = 8888
	client = ChatClient(HOST, PORT)
	client.run()