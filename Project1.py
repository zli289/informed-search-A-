import re
import sys
import time
import math

class Vertice(object):
	def __init__(self,index,SquareX,SquareY):
		self.index=index
		self.SquareX=SquareX
		self.SquareY=SquareY
		self.distance=sys.maxsize
		self.heuristic=sys.maxsize

def getnums(filename):
	it = re.finditer(r"\d+",filename) 
	nums=[]
	for match in it: 
		nums.append(int(match.group()))
	return nums

def readfile(filename):
	file=open(filename,'r')
	data=re.split(r'\n',file.read())
	nums=getnums(filename)

	vertices={}
	for i in data[6:6+nums[0]]:
		paraments=re.split(r'\,',i)
		vertices[int(paraments[0])]=Vertice(int(paraments[0]),int(paraments[1]),int(paraments[2]))

	edges=[{} for i in range(nums[0])]
	for j in data[6+nums[0]+2:6+nums[0]+nums[1]+2]:
		paraments=re.split(r'\,',j)
		x=int(paraments[0])
		y=int(paraments[1])
		distance=int(paraments[2])
		edges[x][y]=distance
		edges[y][x]=distance
		
	return vertices,edges

def extract_min(vertices,g):
	min=sys.maxsize
	node=None
	each=sys.maxsize
	for i in vertices:
		if g:
			each=vertices[i].distance
		else:
			each=vertices[i].heuristic
		if each<min:
			min=each
			node=i
	return node

def reconstruct_path(previous,end):
	result=[]
	while(end!=-1):
		result.append(end)
		end=previous[end]
	return result

def dijkstra(vertices,edges,start,end):
	previous=[-1 for i in vertices]
	vertices[start].distance=0
	while(vertices):
		u=vertices.pop(extract_min(vertices,True))
		if u.index==end:
			print('Cost:',u.distance)
			break
		for index in edges[u.index].keys():
			if index in vertices.keys():
				v=vertices[index]
				uv_distance=edges[u.index][index]

				if  u.distance+uv_distance<v.distance:
					v.distance= u.distance+uv_distance
					previous[index]=u.index
	
	return reconstruct_path(previous,u.index)

def Heuristic(a,b):
	return math.sqrt((a.SquareX-b.SquareX)**2+(a.SquareY-b.SquareY)**2)
	

def Astar(vertices,edges,start,goal):
	openset={}
	previous=[-1 for i in vertices]
	vertices[start].distance=0

	vertices[start].heuristic=Heuristic(vertices[start],vertices[goal])
	openset[start]=vertices[start]

	while(openset.values()):
		u=openset.pop(extract_min(openset,False)) #smallest h value
		if u.index==goal:
			print('Cost:',u.distance)
			break
		del vertices[u.index]

		for index in edges[u.index].keys():
			if index in vertices.keys() and vertices[index] not in openset:
				v=vertices[index]
				uv_distance=edges[u.index][v.index]

				if u.distance+uv_distance < v.distance:
					v.distance=u.distance+uv_distance	
					v.heuristic=Heuristic(v, vertices[goal])+v.distance
					previous[v.index]=u.index
				openset[v.index]=v

	return reconstruct_path(previous,u.index)

def compare(a,b,filename):
	vertices,edges=readfile(filename)
	print('Uninformed Search:')
	start = time.process_time()
	print('Path:',dijkstra(vertices,edges,a,b))
	end = time.process_time()
	print ('Performance:',end-start,'\n')


	vertices,edges=readfile(filename)
	print('Informed Search:')
	start = time.process_time()
	print('Path:',Astar(vertices,edges,a,b))
	end = time.process_time()
	print ('Performance:',end-start)



#a= input('input start:')
#b= input('input end:')
compare(int(10),int(100),'graph1000_50091.txt')