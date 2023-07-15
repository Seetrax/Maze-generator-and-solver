from queue import Queue
import random
from queue import PriorityQueue
def Alltrue(ar,di):#Function to check whether all the elements of ar is true in di
    c=0
    for i in ar:
        if di[i]==False:
            c+=1
    if c==0:
        return True
    else:
        return False
def DFS_explore(k1,adj):#function to expore every possible path from k1
    visited[k1]=True
    tree.append(k1)
    while(Alltrue(adj[k1],visited)==False):
        j=random.choice(adj[k1])
        if visited[j]==False:
            parent[j]=k1
            DFS_explore(j,adj)
def DFS(k,adj):#funtion for dfs exploration
    global visited,parent
    for i in adj:
        visited[i]=False
    ini=k
    visited[k]=True
    tree.append(ini)
    while(Alltrue(adj[ini],visited)==False):
        j=random.choice(adj[ini])
        if visited[j]==False :
            parent[j]=ini
            DFS_explore(j,adj)

class grids:
    def creategrid(self,m):#function to create a grid adjacency graph
        d={}
        for i in range (m):
            for j in range (m):
                ar=[]
                if(j+1)<m:
                    ar.append((i,j+1))
                if(j-1)>=0:
                    ar.append((i,j-1))
                if(i+1)<m:
                    ar.append((i+1,j))
                if(i-1)>=0:
                    ar.append((i-1,j))
                d[(i,j)]=ar
                ar=[]
        return d
    def formgrid(self,m):#dunction to form a grid
        st1="+---"*m+"+"
        st2="|   "*m+"|"
        arr1=[]
        for i in range (m):
            arr1.append(st1)
            arr1.append(st2)
        arr1.append(st1)    
        return arr1
    def form_maze(self,parent,arr):#function to form maze from maze adj list obtained by randomized dfs
        k=len(arr)
        arr2=arr.copy()
        for i in parent:
            if parent[i]!='NULL':
                if parent[i][0]<i[0]:
                    arr2[k-2-2*parent[i][1]]=arr2[k-2-2*parent[i][1]][0:4*(parent[i][0]+1)]+" "+arr2[k-2-2*parent[i][1]][4*(parent[i][0]+1)+1:len(arr2[k-2-2*parent[i][1]])]#going to the row of deletion
                elif parent[i][0]>i[0]:
                    arr2[k-2-2*i[1]]=arr2[k-2-2*i[1]][0:4*(i[0]+1)]+" "+arr2[k-2-2*i[1]][4*(i[0]+1)+1:len(arr2[k-2-2*i[1]])]
                elif parent[i][1]>i[1]:
                    arr2[k-1-2*parent[i][1]]=arr2[k-1-2*parent[i][1]][0:4*parent[i][0]+1]+"   "+arr2[k-1-2*parent[i][1]][4*parent[i][0]+4:len(arr2[k-1-2*parent[i][1]])]
                elif parent[i][1]<i[1]:
                    arr2[k-3-2*parent[i][1]]=arr2[k-3-2*parent[i][1]][0:4*parent[i][0]+1]+"   "+arr2[k-3-2*parent[i][1]][4*parent[i][0]+4:len(arr2[k-3-2*parent[i][1]])]

        return arr2
    def maze_adj(self,parent):#generating maze adjacency dictionary using parent dict produced by dfs
        d={}
        arr5=[]
        for i in parent:
            if parent[i]!='NULL':
                arr5.append(parent[i])
            for j in parent:
                if parent[j]!='NULL':
                    if parent[j]==i:
                        arr5.append(j)
            d[i]=arr5
            arr5=[]

        return d
tree=[]
obj1=grids()
#m=int(input("Enter no"))
visited={}
parent={}
def create_maze(m):
    
    at=obj1.creategrid(m)
    
    for v in at:
        parent[v]="NULL"
    DFS((0,0),at)             
    grid=obj1.formgrid(m)
    #print(parent)
    maze=obj1.form_maze(parent,grid)
    return maze

def print_maze(maze):
    for i in maze:#Printing maze
        print(i)

def print_adj(parent):
    maze_dict=obj1.maze_adj(parent)
    for i in maze_dict:
        print(f"Node {i}: ",end=" ")#Printing adjaceny of a maze
        for j in maze_dict[i]:
            print(f"{j},",end=" ")
        print()
def create_adj(parent):
    maze_dict=obj1.maze_adj(parent)
    return maze_dict
#print_maze(create_maze(m))
#maze_dict=obj1.maze_adj(parent)


def find_path_BFS(ini,adj,final):#Funtion to perform bfs on given maze adjacency dictionary
    visited2={}
    parent2={}
    tree2=[]
    path=[]
    flag=False
    for i in adj:
        visited2[i]=False#Initially make all nodes unvisited and parents of all nodes NULL  
        parent2[i]='NULL'
    q=Queue()#Queue to store an elemnet which is poped and explored every iteration of while
    q.put(ini)
    visited2[ini]=True
    tree2.append(ini)
    while ((q.empty())==False):
        u=q.get()
        if flag==True:break
        for v in adj[u]:
            if visited2[v]==False:
                tree2.append(v)
                visited2[v]=True
                parent2[v]=u
                q.put(v)
                if v==final:
                    flag=True
                    break
    x=final
    path.append(x)
        
    while(parent[x] !=(0,0)): 
        x = parent[x]
        path.append(x)  #  from (2,2) to (0,0)
    path.append((0,0))
    path = path[::-1] 
    return path,len(tree2)


def mandist(k,final):
   
    m2=abs(k[0]-final[0])+abs(k[1]-final[1])
    return m2
def Asearch(ini,adj,final):#Function to perform A* search on maze adjacency dictionary
    path=[]
    visited3={}
    parent3={}
    tree3=[]
    g={}
    flag=False
    for i in adj:
        visited3[i]=False
        parent3[i]='NULL'
        g[i]=0
    q2=PriorityQueue()#Priority queue based on f(n)=no of moves from ini to a state + heurisitc(manhattan distance of node to goal)
    q2.put((g[ini]+mandist(ini,final),ini))

    while ((q2.empty())==False):
        u1=q2.get()
        u=u1[1]
        tree3.append(u)
        visited3[u]=True
        if u==final:
            break
        for v in adj[u]:
            if visited3[v]==False:
                g[v]=g[u]+1#function g here is taken as no of moves required to come from ini to state v 
                parent3[v]=u
                q2.put((g[v]+mandist(v,final),v))
    x=final
    path.append(x)
        
    while(parent3[x] !=(0,0)): 
        x = parent3[x]
        path.append(x)  # backtracking from (2,2) to (0,0)
    path.append((0,0))
    path = path[::-1] 
    return path,len(tree3)
'''p2=find_path_BFS((0,0),maze_dict,(m-1,m-1))
print(f"The path taken is {p2[0]}")
print(f"No of nodes explored : {p2[1]}")'''
