# Import libraries
import pulp
import numpy as np

activities = {}
resources = {}

# Define decision variables
activities = pulp.LpVariable.dicts('Activity duration', activities, lowBound=0)
resources = pulp.LpVariable.dicts('Resource assignment', resources, lowBound=0)

# Define objective function
objective = pulp.LpMaximize(pulp.lpSum(activities.values()))

# Define constraints
# Activity duration constraints
for activity in activities:
    pulp.lpSum([activities[activity]]) <= max_activity_duration

# Resource assignment constraints
for resource in resources:
    pulp.lpSum([resources[resource]]) <= max_resource_capacity

# Total project cost constraint
pulp.lpSum([cost * resources[resource] for resource in resources]) <= max_project_cost

# Create pulp problem
prob = pulp.LpProblem('Cost-time balancing', objective)
prob += activity_duration_constraints
prob += resource_assignment_constraints
prob += total_project_cost_constraint

# Solve problem
status = pulp.LpSolve(prob)

# Print solution
for activity in activities:
    print(f'Activity {activity}: {activities[activity].value()}')
for resource in resources:
    print(f'Resource {resource}: {resources[resource].value()}')