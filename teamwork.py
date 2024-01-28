import networkx as nx

def find_critical_path(activities, dependencies):
    # Create the project network
    project_network = nx.DiGraph()
    for activity, data in activities.items():
        project_network.add_node(activity, duration=data['duration'], cost=data['cost'])
    for dependency in dependencies:
        project_network.add_edge(dependency[0], dependency[1])

    # Calculate the longest path length from every node in the graph
    node_to_longest_path_length = {}
    for node in project_network:
        # Initialize the longest path length to 0
        node_to_longest_path_length[node] = 0

    # Update the longest path length for each node in the graph
    # Update the longest path length for each node in the graph
   # Update the longest path length for each node in the graph
    for node in project_network:
    # Find all simple paths from the node to any other node in the graph
       all_paths = nx.all_simple_paths(project_network, source=node, target=node)

# Check if there are any paths from the node
    # Update the longest path length for each node in the graph
    for node in project_network:
    # Skip nodes that have no incoming or outgoing edges
        if not any(project_network.in_edges(node)) and not any(project_network.out_edges(node)):
            continue

    # Find all simple paths from the node to any other node in the graph
        all_paths = nx.all_simple_paths(project_network, source=node, target=node)
        


    # Check if there are any paths from the node
        if all_paths:
        # Find the longest path from the node to any other node
                longest_path = max(all_paths, key=len)
              
        # Calculate the duration of the longest path
                path_duration = sum(p["duration"] for p in longest_path)
        # Update the longest path length for the node
                node_to_longest_path_length[node] = path_duration
            
        else:
        # If there are no paths from the node, set the longest path length to 0
            node_to_longest_path_length[node] = 0

            
    critical_path = []
    for node in node_to_longest_path_length:
        if node_to_longest_path_length[node] == nx.dag_longest_path_length(project_network, weight='duration'):
            critical_path.append(node)

    return critical_path

activities = {
    'A': {'duration': 5, 'cost': 10},
    'B': {'duration': 10, 'cost': 8},
    'C': {'duration': 13, 'cost': 12},
    'D': {'duration': 3, 'cost': 4},
    'E': {'duration': 9, 'cost': 6},
    'F': {'duration': 10, 'cost': 5},
    'G': {'duration': 5, 'cost': 9},
}

# تعریف رابطه‌ها بین فعالیت‌ها
dependencies = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('D', 'E'),
    ('C', 'F'),
    ('F', 'G'),
    ('E', 'G')
]


# Call the function and print the critical path
critical_path = find_critical_path(activities, dependencies)
print("The critical path is:")
for node in critical_path:
     print(node)
print(critical_path)    
