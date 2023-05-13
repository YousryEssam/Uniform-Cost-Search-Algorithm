from queue import PriorityQueue
def uniform_cost_search(graph, start, goal):
    visited = set()  # set of visited nodes
    frontier = PriorityQueue()  # priority queue for nodes to explore
    frontier.put((0, start))  # (priority, node) tuple, priority is the cost
    came_from = {}  # dictionary to store the path

    # Initialize the cost of reaching start node to 0
    cost_so_far = {start: 0}

    while not frontier.empty():
        current_cost, current_node = frontier.get()

        if current_node == goal:
            # Reached the goal node
            break

        visited.add(current_node)

        for next_node, edge_cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + edge_cost

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                frontier.put((priority, next_node))
                came_from[next_node] = current_node

    # Reconstruct the path from start to goal
    path = []
    total_cost = 0
    if goal in came_from:
        current = goal
        while current != start:
            path.append(current)
            total_cost += graph[came_from[current]][current]
            current = came_from[current]
        path.append(start)
        path.reverse()

    return path, total_cost

# Graph representation of the Romanian Map 
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Eforie': {'Hirsova': 86}
}

start_node = 'Bucharest'
goal_node = 'Arad'
result, total_cost = uniform_cost_search(graph, start_node, goal_node)
print ("Start State : " , start_node , "\nTarget State : " ,goal_node)
print("Path:", result)
print("Total Cost:", total_cost) 