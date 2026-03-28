# Delivery Optimization Task

## Problem Statement
The goal of this project is to assign delivery locations to 3 agents in an optimized way based on priority and distance.

## Approach Used

1. First, the input CSV file is read using pandas.
2. The priority values (High, Medium, Low) are converted into numeric form:
   - High = 1
   - Medium = 2
   - Low = 3

3. The data is sorted based on:
   - Priority (higher priority first)
   - Distance (shorter distance first)

4. Deliveries are assigned using a greedy approach:
   - Each delivery is given to the agent who has the least total distance so far.

5. This helps in balancing the workload among all agents.

## Output
- A new column called `AssignedAgent` is added.
- The final result is saved in `output.csv`.
- Total distance and tasks for each agent are printed.

## Algorithm
Greedy Load Balancing Algorithm

## Files Included
- main.py (source code)
- input.csv (input data)
- output.csv (result)
- README.md (documentation)

## Conclusion
This method ensures that high priority deliveries are completed first and the total distance is distributed evenly among agents.