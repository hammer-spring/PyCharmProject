#!/usr/bin/python  
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

#本文件演示如何构造一个图，即networkx中的graph对象
def generateGraph(func, n):
	"""图生成函数，为了使该函数具有扩展性，
	我们用func作为函数参数，该函数可以决定生成何种类型的图
	"""
	G = func(n)
	return G

def loadGraph(graphfile):
	"""使该函数从文件从读入信息，创建一个graph对象，
	这里我们使用gml格式文件作为输入
	"""
	G = nx.read_gml(graphfile)
	return G
