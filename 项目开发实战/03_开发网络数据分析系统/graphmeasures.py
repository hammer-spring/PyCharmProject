#!/usr/bin/python  
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import graphgenerator

def calcPagerank(G, alpha=0.85, max_iter=100, tol=1e-06):
	"""计算图种每个节点的PageRank值
	这里直接调用networkx中的pagerank函数
	"""
	pr = nx.pagerank(G, alpha, None, max_iter, tol)
	return pr

def calcCentrality(G, label):
	"""计算不同形式的centrality值
	根据label的不同，可以计算三种centrality：
	degree centrality，betweenness centrality以及closeness centrality
	"""
	if label == 'degree':
		return nx.degree_centrality(G)
	elif label == 'betweenness':
		return nx.betweenness_centrality(G)
	elif label == 'closeness':
		return nx.closeness_centrality(G)
	else:
		print('Not support type...')

def plotGraph(G, graphmeasure, size):
	"""给定图的度量指标
	根据指标的数值大小，绘制出该图
	度量值更大的节点在可视化中会表现为更大的点
	"""
	node_sizes = dict.fromkeys(G.nodes(), 0.005)
	# Make node size of giant component nodes proportional to their eigenvector
	for k, v in graphmeasure.items():
	    node_sizes[k] = round(v, 6)
	#size参数用来对度量值进行比例放缩
	node_sizes = [v*size for v in node_sizes.values()]

	nx.draw(G, font_size=10, node_size=node_sizes, vmin=0.0, vmax=1.0)#, with_labels=True)
	plt.show()


if __name__ == '__main__':
	G = graphgenerator.loadGraph('lesmiserables.gml')
	pr = calcPagerank(G)
	plotGraph(G, pr, 5000)

	centrality = calcCentrality(G, 'closeness')
	plotGraph(G, centrality, 250)

	centrality = calcCentrality(G, 'degree')
	plotGraph(G, centrality, 500)