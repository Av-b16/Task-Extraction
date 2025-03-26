def categorize_tasks(tasks):
    categorized_tasks = []
    for task in tasks:
        category = "General"
        if "review" in task["task"].lower():
            category = "Work"
        elif "buy" in task["task"].lower() or "purchase" in task["task"].lower():
            category = "Shopping"
        elif "submit" in task["task"].lower():
            category = "Submission"

        task["category"] = category
        categorized_tasks.append(task)

    return categorized_tasks
