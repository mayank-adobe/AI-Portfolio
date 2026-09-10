# Week 2 Day 4

project = {
    "project_name": "Workfront Planning Automation",
    "priority": "High",
    "owner": "Mayank Saxena",
    "active": True,
    "tasks": [
        "Requirement Gathering",
        "Project Creation",
        "Planning Record Update"
    ],
    "risks": ["Missing requirements",
              "Timeline delay"
              ]
}

print("Project Details")
print("----------------")

print(f"Project Name : {project['project_name']}")
print(f"Priority     : {project['priority']}")
print(f"Owner        : {project['owner']}")
print(f"Active       : {project['active']}")

print("\nTasks")

if project["priority"] == "High":
    print("Status : Urgent Project")

elif project["priority"] == "Medium":
    print("Status : Important Project")

else:
    print("Status : Normal Project")

for task in project["tasks"]:
    print(f"- {task}")

print("\nRisks")

for risk in project["risks"]:
    print(f"- {risk}")

if len(project["tasks"]) > 2:
    print("\nLarge Project")
else:
    print("Small Project")
