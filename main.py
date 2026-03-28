import pandas as pd

# dataset path
df = pd.read_csv("input.csv")

# Converting variables to rank
priority_map = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

df["PriorityValue"] = df["Priority"].map(priority_map)

# Sorting based on priority and distance
df = df.sort_values(by=["PriorityValue", "Distance"])

# 3 agents
agents = {
    "A1": {"distance": 0, "tasks": []},
    "A2": {"distance": 0, "tasks": []},
    "A3": {"distance": 0, "tasks": []}
}

assigned_list = []

# Assigning delievery
for i, row in df.iterrows():

    chosen_agent = min(agents, key=lambda x: agents[x]["distance"])


    agents[chosen_agent]["tasks"].append(row["LocationID"])
    agents[chosen_agent]["distance"] += row["Distance"]

    assigned_list.append(chosen_agent)

df["AssignedAgent"] = assigned_list

df.drop(columns=["PriorityValue"], inplace=True)

df.to_csv("output.csv", index=False)

print("\nDelivery Plan:\n")
print(df)

print("\nSummary:\n")
for agent in agents:
    print(agent,"-> Total Distance:",
        agents[agent]["distance"],"| Deliveries:",
        agents[agent]["tasks"]
    )