# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import graphgenerator

def plotDegree(G):
	deg = nx.degree(G) #取得每个节点的度
	sorted_degree = sorted(deg.values(), reverse=True)
	
	plt.figure(figsize=(10,10))
	p1 = plt.subplot(221)
	p2 = plt.subplot(222)
	
	#子图1绘制图的度分布直方图
	p1.hist(list(deg.values()))
	p1.set_title("Degree histogram")
	p1.set_xlabel("Degree")
	p1.set_ylabel("Number of Subjects")

	#子图2绘制图的度对数分布图
	p2.loglog(sorted_degree,'r-',marker='*', markersize=10)
	p2.set_title("Degree rank plot")
	p2.set_xlabel("Rank")
	p2.set_ylabel("degree")
	
	#子图3直接绘制出当前的graph
	p3 = plt.subplot(212)
	p3.set_title("Network plot")
	nx.draw(G,node_size=25)

	plt.show()

if __name__ == '__main__':
	#简单起见我们使用《悲惨世界》人物关系图来进行演示
	G = graphgenerator.loadGraph('lesmiserables.gml')
	plotDegree(G)