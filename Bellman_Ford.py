import csv
from collections import deque
import string

# Reading the data and creating the data structures
files = ['matrix_100_1_3_1.txt','matrix_100_1_3_2.txt']
for f in files:
      with open(f+".gr") as inputfile:
            Adjacency_List = {}
            W = {}                                                       
            for line in inputfile:
                  l = line.split(' ')
                  if l[0] == 'p':
                        vertices = int(l[2])
                        edges = int(l[3])
                  elif l[0] == 'a':
                        W[int(l[1]),int(l[2])] = int(l[3])
                        T = int(l[1])
                        H = int(l[2])
                        if T not in Adjacency_List:           #creating the adjacency list by appending both T and H as total vertices as the graph is undirected
                              Adjacency_List[T] = []
                        Adjacency_List[T].append(H)
            for v in range(1,vertices+1):
                  if v not in Adjacency_List:
                        Adjacency_List[v] =[]

      
      def Bellman_Ford(G,s):
            dist = {}
            dist[s]= 0
            pred = {}
            pred[s] = 0
            N = list(range(1,vertices+1))
            N.remove(s)
            for i in N:
                  dist[i] = int(vertices*max(W.values()))
                  pred[i] = -1
            for i in range(1,vertices+1):
                        for j in G[i]:
                              if dist[j] > dist[i] + W[i,j]:
                                    dist[j] = dist[i] + W[i,j]
                                    pred[j] = i
            return dist,pred
      s = 1
      D,P = Bellman_Ford(Adjacency_List,s)
      filename = f[:-4]
      out_file = filename + ".csv"
      with open(out_file, 'wb') as outfile: 
          filewriter = csv.writer(outfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
          fieldnames = ['Vertex', 'Distance','Predecessor'] 
          writer = csv.DictWriter(outfile, fieldnames = fieldnames)
          writer.writeheader()
          writer.writerows({'Vertex':  str(key),'Distance': str(D[key]), 'Predecessor': str(P[key])} for key in D)
