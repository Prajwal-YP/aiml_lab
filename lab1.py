def astar(startnode,endnode):
    
    openset     = set(startnode)
    closedset   = set()
    g           = {}
    parent      = {}
    
    g[startnode]        = 0
    parent[startnode]   = startnode
    
    while len(openset)>0:
        n=None
        for v in openset: 
            if n==None or g[v]+h(v)<g[n]+h(n):
                n=v
            
        if n==endnode or graphnode[n]==None:
            pass
        else:
            for (m,weight) in neighbors(n):
                if m not in openset and m not in closedset:
                    openset.add(m)
                    parent[m]  = n
                    g[m]       = g[n] + weight
                else:
                    if g[n]+weight<g[m]:
                        g[m]=g[n]+weight
                        parent[m]=n
        if n==None:
            print("Path does not exists!!")
            return
        
        if n==endnode:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n= parent[n]
            path.append(startnode)
            path.reverse()
            print(path)
            return
                
        openset.remove(n)
        closedset.add(n)
        
    print("Path does not exists!!")
    return
                        
                    
def neighbors(x):
    if x in graphnode:
        return graphnode[x]
    else:
        return None
        
def h(x):
    h_dict =    {
                    'A': 1,
                    'B': 1,
                    'C': 1,
                    'D': 1,
                    'E': 1,
                    'F': 1
                }
    return h_dict[x]

graphnode = {
                'A' : [('B',2),('C',3)],
                'B' : [('D',2)],
                'C' : [('E',1)],
                'D' : [('F',3)],
                'E' : [('F',2)],
            }

graphnode = {
                'A' : [('B',4),('C',2)],
                'B' : [('D',2),('E',2)],
                'C' : [('B',1)],
                'D' : [('F',3)],
                'E' : [('F',2)]
            }

astar("A","F")