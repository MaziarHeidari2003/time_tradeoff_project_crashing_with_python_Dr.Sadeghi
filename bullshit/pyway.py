# Import necessary modules
import networkx as nx
from datetime import datetime as dt

# Create the project schedule as a directed acyclic graph (DAG)
project_network = nx.DiGraph()

# Add nodes to the graph, representing project tasks
project_network.add_nodes_from(['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7', 'task8'])

# Add edges to the graph, representing task dependencies and durations
project_network.add_edges_from([
    ('task1', 'task2', {'duration': 5}),
    ('task1', 'task3', {'duration': 4}),
    ('task2', 'task4', {'duration': 3}),
    ('task2', 'task5', {'duration': 2}),
    ('task3', 'task6', {'duration': 6}),
    ('task3', 'task7', {'duration': 7}),
    ('task4', 'task8', {'duration': 1}),
    ('task5', 'task8', {'duration': 1})
])

# Calculate the critical path of the project schedule
# Calculate the critical path of the project schedule
critical_path_length = nx.dag_longest_path_length(project_network, weight='duration')

# Identify the critical path tasks
critical_path_tasks = []
for node in nx.topological_sort(project_network):
    path_length = nx.dag_longest_path_length(project_network, node=node, weight='duration')
    if path_length == critical_path_length:
        critical_path_tasks.append(node)

# Print the critical path tasks
print(f'Critical path tasks: {critical_path_tasks}')


# Print the critical path length
print(f'Critical path length: {critical_path_length} days')

# Identify the critical path tasks
for node in nx.topological_sort(project_network):
    if nx.dag_longest_path_length(project_network, source=node, weight='duration') == critical_path_length:
        print(f'{node} is a critical path task')