#!/usr/bin/python  
# -*- coding: utf-8 -*-

import community
import networkx as nx
import matplotlib.pyplot as plt
import graphgenerator

def communityDetectioin(G):
	"""社区发现（community detection）函数
	简单起见，我们在这里直接调用community库里的best_partition方法
	"""
	communities = community.best_partition(G)
	return communities


if __name__ == '__main__':
	G = graphgenerator.loadGraph('lesmiserables.gml')
	communities = communityDetectioin(G)

	#用不同的颜色绘制属于不同的社区的节点
	plt.figure(figsize=(16, 9))
	color = ['y', 'g', 'r', 'k', 'm', 'b', 'c']
	idx = 0
	pos = nx.spring_layout(G)
	for com in set(communities.values()) :
	    list_nodes = [nodes for nodes in communities.keys()
	                                if communities[nodes] == com]
	    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 50,
	                                node_color = color[idx])
	    idx += 1

	nx.draw_networkx_edges(G, pos, alpha=0.5)
	plt.show()