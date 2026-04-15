class graph:
    def __init__(self,directed,weight):
        self.weight=weight
        self.directed=directed
        self.graphdict={}
    def add_node(self,Nodename):
        if Nodename not in self.graphdict:
            self.graphdict[Nodename]=[]
        else:
            return 'already name exist'
    def add_edge(self,node1,node2,weight):
        if node1 not in self.graphdict:
            return node1
        if node2 not in self.graphdict:
            return node2
        if self.directed==False:
            self.graphdict[node1].append((node2,weight))
            self.graphdict[node2].append((node1,weight))
        else:
            self.graphdict[node1].append((node2,weight))

g1=graph(False,False)
g1.add_node('A')
g1.add_node('B')
g1.add_node('C')
g1.add_node('D')
g1.add_node('E')

g1.add_edge('A','B',-1)
g1.add_edge('A','C',-1)
g1.add_edge('A','D',-1)
g1.add_edge('B','D',-1)
g1.add_edge('E','D',-1)
g1.add_edge('C','D',-1)
g1.add_edge('D','D',-1)

for key,value in g1.graphdict.items():
    print(key+ ' ->', end=(' '))
    for i in value:
        print(str(i[0])+ ':'+'weight :'+str(i[1]),end=(' '))
    print('')




g2=graph(False,True)
g2.add_node('A')
g2.add_node('B')
g2.add_node('C')
g2.add_node('D')
g2.add_node('E')

g2.add_edge('A','B',6)
g2.add_edge('A','D',1)
g2.add_edge('B','C',5)
g2.add_edge('B','E',4)
g2.add_edge('C','E',5)
g2.add_edge('D','B',2)
g2.add_edge('D','E',1)
g2.add_edge('E','B',2)

for key,value in g2.graphdict.items():
    print(key+ ' ->', end=(' '))
    for i in value:
        print(str(i[0])+ ':'+'weight :'+str(i[1]),end=(' '))
    print(' ')


