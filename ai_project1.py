
import numpy as np
import heapq as hq
import time

puzzle=[]
goal=[]
operators=["UP","RIGHT","DOWN","LEFT"]# Try combinations of operator sequence (gives different search ways)



class Node:
  def __init__(self,arr,root=None):
    self.state= arr
    self.root =root
    self.child=[]
    self.depth=0
    self.goal_cost=0
  def add(self,node,depth=1):
    node.root=self
    self.child.append(node)
    node.depth=self.depth+depth
  def __eq__(self, second):
    # overrid equal operator in heapq

    return self.state.tolist()==second.state.tolist() #np.array_equal(self.state, second.state) #(self.state == second.state).all()
    
  def __lt__(self, second):
     #override less than operator in heapq
    return (self.depth + self.goal_cost) < (second.depth + second.goal_cost)
  def expand(self,operators):
    #expand current nodes with 4 operators
    i,j= map(int,np.where(self.state == 0)) #find position of blank tile
    len_states=len(self.state)

    expanded_states=[]
    for op in operators:

      if op == "UP": #if operator is UP then swap blank tile with element above and add state in expanded list
        
        if i!=0: #check if we are not in first row
          tmp=self.state.copy() #create copy current state
          tmp[i][j], tmp[i - 1][j] = tmp[i - 1][j],tmp[i][j] #swap
          if self.root and (tmp == self.root.state).all(): #dont add if expanded state is same as parent state 
            continue #expanded_states.append(None) 
          else:
            expanded_states.append(tmp)
      if op =="RIGHT":  #if operator is RIGHT then swap blank tile with right element and add state in expanded list
        
        if j!=(len_states-1):   #check if we are not in last column
          tmp=self.state.copy() 
          tmp[i][j],tmp[i][j+1]= tmp[i][j+1],tmp[i][j]
          
          if self.root and (tmp == self.root.state).all():
            continue 
          else:
            expanded_states.append(tmp)
      if op =="DOWN":  #if operator is DOWN then swap blank tile with element below and add state in expanded list

        if i!=(len_states-1): #check if we are not in last row
          tmp=self.state.copy()
          tmp[i][j],tmp[i + 1][j]= tmp[i + 1][j],tmp[i][j]
          
          if self.root and (tmp == self.root.state).all():
            continue 
          else:
            expanded_states.append(tmp)
      if op=="LEFT":  #if operator is LEFT then swap blank tile with left element and add state in expanded list
        if j!=0:  #check if we are not in first column
          tmp=self.state.copy()
          tmp[i][j],tmp[i][j-1]= tmp[i][j-1],tmp[i][j]
          
          if self.root and (tmp == self.root.state).all():
            continue
          else:
            expanded_states.append(tmp)

    
    return expanded_states

  def calculate_misplaced_tiles(self,goal):
  # calculate count of misplaced tiles
    self.goal_cost= np.sum((self.state != goal) & (self.state != 0), where=(self.state != goal) & (self.state != 0))#np.sum((self.state!=goal)& (self.state != 0)) # check which all elements (ignore the blank tile '0') from curr_state are not equal to goal 


  def calculate_manhattan(self,goal):
    # calculate manhattan distance between positions of elements in curr_state which are not equal to goal
    manhattan_distance=0 # initialize
    md=np.where(self.state!=goal) # get the indices of elements in curr_state which do no match the goal
    for m,d in zip(md[0],md[1]): #iterate over the above indices
      if self.state[m][d]!=0: #skip blank
        goal_loc=np.argwhere(goal==self.state[m][d]) # find the location of element in goal
        curr_index=np.array([m,d]) #convert to numpy array 
        manhattan_distance+=np.sum(abs(goal_loc - curr_index)) #find abs difference between the goal and curr_state positions
    self.goal_cost =manhattan_distance 


def general_search(puzzle,goal,maxIterations=10000): #general_search by default is Uniform Cost Search where we consider goal heuristic as 0
  root=Node(puzzle) #create root object of Node from input puzzle
  queue=[] # main queue to store the nodes
  hq.heappush(queue,root) # heap queue is use to prioritize the heuristic
  
  visited=[] #visited nodes array to check if state is already explored in parent

  maxNode=1 # variable to track number of nodes in queue
  expanded=0 # counter for number of expanded nodes
  mi=0 # counter to check number of iterations
  maxDepth=0
  while mi<maxIterations: # Loop runs till the maxIterations. If goal found before then code returns
    maxNode= max(len(queue),maxNode)
    curr= hq.heappop(queue)#queue.pop(0)

    maxDepth=curr.depth
    if (curr.state==goal).all(): #Check if we reached goal
      return expanded,maxNode, maxDepth #Return number of expanded nodes, max nodes in queue and depth reached
    else:
      visited.append(curr) #add current to visited

      
      expanded_list = curr.expand(operators) #expand current with operators

      if expanded_list==[]: # no nodes in expanded list
        continue
      
      for exp_state in expanded_list: #iterate expanded states
        new_state= Node(exp_state) # create new node from expanded state


        if ((new_state in queue ) or (new_state in visited)): #skip the node if  already in queue or visited 
          continue
        if (algo == "A*"): # use misplaced tiles heuristic if algo is A*

          new_state.calculate_misplaced_tiles(goal)


        if (algo == "AMAN"): #use manhattan distance heuristic if algo is AMAN
          new_state.calculate_manhattan(goal)
 
        curr.add(new_state) #Add child to the parent node
        hq.heappush(queue,new_state) #add new child to queue

        #print(f"Heuristic COST: {new_state.start_cost+new_state.goal_cost}") #uncomment to print heuristic cost at each node expansion
      expanded+=1 #increment expanded nodes
      mi+=1 #increment counter
  
  return -1,expanded,maxNode,maxDepth

def printify_puzzle(arr):
  return str(arr).replace('[', '').replace(']', '').replace('\n ','\n')




  # get input from input file and goal from goal file and convert it numpy array
with open("input.txt") as f:
  for line in f:

    puzzle.append(list(map(int,line.split(" "))))#np.vstack((inp,list(map(int,line.split(" ")))))
  
with open("goal.txt") as f:
  for line in f:
    goal.append(list(map(int,line.split(" "))))#np.vstack((inp,list(map(int,line.split(" ")))))


puzzle= np.array(puzzle)
goal = np.array(goal)
print("Enter Choice of algorithm (enter abbrevation): \n'UCS: Uniform Cost Search'\n'A*: Misplaced Tile heuristic'\n'AMAN: A* Manhattan heuristic'")
algo= input()
print("Enter Max Iterations for which algorithm can try searching (leave blank to consider default 10000 iterations)")
maxIterations= input()
maxIterations=int(maxIterations if maxIterations.isnumeric() else 10000)

start_time=time.perf_counter()    
output=general_search(puzzle,goal)
end_time= time.perf_counter()
if output[0]==-1:
  print(f"Search Limit crossed. Expanded Nodes: {output[1]}\nNumber of nodes in queue: {output[2]}\nDepth: {output[3]} " )
else:
  print(f"Goal Reached!!!\nExpanded Nodes: {output[0]}\nNumber of nodes in queue: {output[1]}\nDepth: {output[2]} " )
solution_time=end_time-start_time

#converts time execution to simple interpretation
if solution_time<1:
  solution_time_str= str(round(solution_time*1000,2)) + " milliseconds"
else:
  solution_time_str = str(solution_time) +" seconds"
                    
print(f"Time required for {algo} to solve \n{printify_puzzle(puzzle)}\nis {solution_time_str} ")

