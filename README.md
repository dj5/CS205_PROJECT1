# CS205_PROJECT1
### Name: Dhananjay Gavade
### SID: 862395404
### email: dgava001@ucr.edu

#### Code Exection Steps:

1. Enter puzzle in input.txt.
2. If you want to change goal state, write in goal.txt
3. Run ai_project1.py or use the notebook AI_Project1.ipynb

#### Algorithms:
##### Uniform Cost Search: 
Implemented general search algorithm which considers h(n)=0 for uniform cost search. I have used heapq to store the nodes and numpy array to store the states. 'general_search' function takes the puzzle as input and uses 'operator' list to expand nodes based on given operations. User can customize the sequence of these operators in the list. Change of sequence may result in different results.
##### A* Misplaced Tiles:
This algorithm is implemented by using a heuristic function that calculates the count of misplaced tiles and passes the heuristic value to general_search. Count is calculated using numpy's array comparison and sum function in a single line. While checking the misplaced tiles, blank tile is ignored in the count.

##### A* Manhattan Distance Heuristic:
This algorithm is implemented by using a heuristic function that calculates the Manhattan distance between positions misplaced elements in current state compared to goal state. Distance is calculated and passed to general_search, which adds the heuristic value to the node. Based on heuristic value the nodes are prioritized  in the heap queue.
#### References:
[1] Numpy - https://numpy.org/devdocs/user/index.html
[2] HeapQ - https://docs.python.org/3/library/heapq.html
[3] Time - https://docs.python.org/3/library/time.html
[4] A* - https://www.geeksforgeeks.org/a-search-algorithm/

