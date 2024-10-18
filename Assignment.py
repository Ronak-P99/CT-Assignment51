import time

def schedule_tasks(task):
    if isinstance(task, dict):
        # Check if it contains 'subtasks' that need processing
        if 'subtasks' in task:
            # Recursively process each subtask, but only process dictionaries
            task['subtasks'] = [schedule_tasks(subtask) for subtask in task['subtasks']]
            
            # Sort subtasks by 'priority' if they are dictionaries
            task['subtasks'].sort(key=lambda x: x['priority'] if isinstance(x, dict) else float('inf'))
        
        # Return the processed dictionary
        return task
    
    # If the task is not a dictionary (base case for recursion), return it as-is
    return task

tasks = {
    'id': 1,
    'name': 'Main Task',
    'priority': 2,
    'subtasks': [
        {
            'id': 2,
            'name': 'Subtask 1',
            'priority': 3,
            'subtasks': ["task1", "task2"]
        },
        {
            'id': 3,
            'name': 'Subtask 2',
            'priority': 1,
            'subtasks': ["task1", "task2"]
        }
    ]
}
start_time = time.time()
sorted_tasks = schedule_tasks(tasks)
end_time = time.time()
print(sorted_tasks)
print("Time taken for recursive function:", end_time - start_time)
