# Week 2 Day 3

project = {
    "project_name": "Workfront Planning Automation",
    "priority": "High",
    "owner": "Mayank Saxena",
    "active": True,
    "tasks": [
        "Requirement Gathering",
        "Project Creation",
        "Planning Record Update"
    ]
}

print("Project Details")
print("----------------")

print(f"Project Name : {project['project_name']}")
print(f"Priority     : {project['priority']}")
print(f"Owner        : {project['owner']}")
print(f"Active       : {project['active']}")

print("\nTasks")

for task in project["tasks"]:
    print(f"- {task}")
