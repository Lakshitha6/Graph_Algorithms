# Graph Traversal Algorithms

### Graph 

<img width="1175" height="571" alt="graph" src="https://github.com/user-attachments/assets/ca1de59c-f15a-4ac4-ae53-146e344dcefa" />



## BFS (Breadth-First Search) Execution Flow

The Broad-First Search algorithm in `bfs.py` implementation follows these steps:

1.  **Initialization**:
    - The `breadth_first_search` function starts with a specific `vertex`.
    - It initializes a `visited` list and a `queue`, both containing the start `vertex`.

2.  **Traversal Loop**:
    - The algorithm runs a `while` loop as long as the `queue` is not empty.
    - **Dequeue**: It removes the *first* element from the queue (`queue.pop(0)`) to process it. This First-In-First-Out (FIFO) behavior is examining the graph layer by layer.

3.  **Neighbor Processing**:
    - For the processed node, it retrieves all its neighbors (adjacent vertices).
    - **Randomization**: The order of neighbors is shuffled using `random.shuffle`. This means the traversal path may vary between runs if a node has multiple unvisited neighbors.
    - It iterates through each neighbor:
        - If the neighbor has **not** been visited yet:
            - It is added to the `queue` (for future processing).
            - It is marked as `visited` immediately.

## DFS (Depth-First Search) Execution Flow

The Depth-First Search algorithm in `dfs.py` implementation allows these steps:

1.  **Initialization**:
    - The `depth_first_search` function initializes a `visited` list and a `stack`, both containing the starting `vertex`.

2.  **Traversal Loop**:
    - The algorithm runs a `while` loop as long as the `stack` is not empty.
    - **Pop**: It removes the *last* element from the stack (`stack.pop()`). This Last-In-First-Out (LIFO) behavior explores as deep as possible along each branch before backtracking.

3.  **Neighbor Processing**:
    - Similar to BFS, it retrieves and shuffles the neighbors.
    - It iterates through each neighbor:
        - If the neighbor has **not** been visited yet:
            - It is added to the `stack`.
            - It is marked as `visited` immediately (upon discovery, rather than upon processing).
