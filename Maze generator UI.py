from tkinter import *
import Maze
root =Tk()
root.title("Maze generator")
canvas_height=600
canvas_width=600
mycanvas=Canvas(root,width=canvas_width,height=canvas_height)
mycanvas.pack()
maze=[]
dic={}

def pprint(maze):
    global root,mycanvas,dic
    h=len(maze)
    w=len(maze[0])
    he=canvas_height/h
    we=canvas_width/w
    
    for i in range(len(maze)):
        
        for j in range( len(maze[i])):
            if maze[i][j]!=' ':
                mycanvas.create_rectangle(j*we,i*he,(j*we+we),i*he+he,fill="green",outline="green")

                #mycanvas.create_rectangle(j*we,canvas_height-i*he,j*we+we,canvas_height-i*he-he,fill="green",outline="green")
            elif maze[i][j]==' ':
                

                mycanvas.create_rectangle(j*we,i*he,j*we+we,i*he+he,fill="white",outline="white")
        
    
        
                
def fill_path(tup,maze,color):
    global root,mycanvas
    h=len(maze)
    w=len(maze[0])
    he=canvas_height/h
    we=canvas_width/w
    '''for k in tup:
        for (j,i) in dic[k]:
            if maze[i][j]==' ':
                mycanvas.create_rectangle(j*we,i*he,j*we+we,i*he+he,fill="blue",outline="blue")'''
    for i in range(len(maze)):
        for j in range( len(maze[i])):
            if maze[i][j]==' ' and ((j-1)//4,(h-i-1)//2) in tup:
                #print(((j)//4,(i)//3))

                    mycanvas.create_rectangle(j*we,i*he,j*we+we,i*he+he,fill=color,outline=color)   
           
def find_path1():
    global maze

    tup=Maze.find_path_BFS((0,0),Maze.create_adj(Maze.parent),(int(e.get())-1,int(e.get())-1))
    
    fill_path(tup[0],maze,"light blue")
    print(f"{tup[1]} nodes were explored using BFS search")
def find_path2():
    global maze

    tup=Maze.Asearch((0,0),Maze.create_adj(Maze.parent),(int(e.get())-1,int(e.get())-1))
    
    fill_path(tup[0],maze,"yellow")
    print(f"{tup[1]} nodes were explored using A* search")
def clicked():
    global maze,dic
    if int(e.get())>40:
        return 0
    
    Maze.parent={}
    Maze.visited={}
    maze=Maze.create_maze(int(e.get()))
    
    for i in range(int(e.get())):
        for j in range(int(e.get())):
            dic[(i,j)]=[]
    pprint(maze)
    h=len(maze)
    w=len(maze[0])
    he=canvas_height/h
    we=canvas_width/w
    
    
    #Maze.print_maze(maze)
    
    '''But1=Button(root,text="Press",command=clicked,fg='yellow',bg='black')
    But1.pack()
    But1=Button(root,text="Press",command=clicked,fg='yellow',bg='black')
    But1.pack()'''
myLabel=Label(root,text="Enter the value of n to create a nxn maze : (Less than 40)")
myLabel.pack()
e=Entry(root,width=50,borderwidth=5)
e.pack()

But1=Button(root,text="Generate Maze",command=clicked,fg='yellow',bg='black')
But1.pack()
But2=Button(root,text="Solve by BFS",command=find_path1,fg='yellow',bg='black')
But2.pack()
But2=Button(root,text="Solve by A* search",command=find_path2,fg='yellow',bg='black')
But2.pack()
root.mainloop()
    
