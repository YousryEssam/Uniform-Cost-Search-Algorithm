# AI_Project Simple project ( Uniform Cost Search - Romanian Map )


# Romaina Map 

![Romania map](https://user-images.githubusercontent.com/43790152/97784960-1a142580-1bc4-11eb-9070-39c03eb16df2.png)

<br>

This code implements the Uniform Cost Search algorithm to find the optimal path and total cost from a start node to a goal node in the Romanian map. The Romanian map is represented as a graph with nodes as cities and edges as the distances between cities.

## Algorithm Overview

The Uniform Cost Search algorithm explores the graph by considering the cumulative cost of each path. It starts from the start node and expands the nodes with the lowest cumulative cost first. This ensures that when the goal node is reached, the accumulated cost is the minimum among all possible paths.

The algorithm uses a priority queue to store the nodes to be explored, with the priority being the cumulative cost. It keeps track of the visited nodes, the path from the start node to each explored node, and the cost of reaching each node from the start node. The algorithm continues until it reaches the goal node or exhausts all possible paths.

## Complexity

The time and space complexity of the algorithm are as follows:

- Time Complexity: The time complexity of the algorithm is O((|V| + |E|)log|V|), where |V| is the number of nodes (vertices) and |E| is the number of edges in the graph. The priority queue operations take O(log n) time, where n is the number of elements in the queue.

- Space Complexity: The space complexity is O(|V|), where |V| is the number of nodes in the graph. This includes the space required for storing the visited nodes, frontier, dictionaries, and the path.

## Constraints

- The code assumes that the input graph is a directed weighted graph.
- The edge costs must be non-negative integers or floats.
- The start node and goal node should be present in the graph.
- The code does not handle cases where there are multiple paths with the same cost. It will return any valid path with the minimum cost.

## Usage

1. Install Python: Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Clone the repository: Clone this repository to your local machine using the following command:

3. Navigate to the directory: Change your current directory to the cloned repository's location:

4. Run the code: Execute the code using the following command:

5. Explore the results: The code will print the start state, target state, the path from the start to the goal state, and the total cost. You can modify the `start_node` and `goal_node` variables in the code to specify your desired start and goal states.

Note: The code includes the graph representation of the Romanian map, but you can modify it or provide your own graph if needed.

<br>

👉 Don't for get to ⭐ the repo!

## 👨‍💻‍ About author

### Yousry Essam 

[![LinkedIn Link](https://img.shields.io/badge/Connect-Yousry-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect
)](https://www.linkedin.com/in/yousryessam/)

Follow me on GitHub:

[![GitHub Follow](https://img.shields.io/badge/Connect-Yousry-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/YousryEssam)

Copyright (c) 2023 Yousry Essam 
