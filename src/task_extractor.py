import re

# Updated regex to detect names and deadlines
PERSON_PATTERN = r'\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)\b'

# Task patterns to identify actions
TASK_PATTERNS = [
    r'\b(has to|needs to|should|must|is supposed to)\s(.+?)(by|before|at|on|until|$|\.)',  # Task with a deadline
    r'\b(has to|needs to|should|must|is supposed to)\s(.+?)($|\.)'                         # Task without a deadline
]

# Deadline pattern to identify due dates
DEADLINE_PATTERN = r'\b(by|before|at|on|until)\s(.+?)(\s|\.|$)'

# Extract tasks from sentences and associate them with names
def extract_task(sentences):
    tasks = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        
        # Find all person names from the sentence
        person_matches = re.findall(PERSON_PATTERN, sentence)
        
        # Extract task matches from sentence
        task_matches = re.finditer('|'.join(TASK_PATTERNS), sentence, re.IGNORECASE)

        for task_match in task_matches:
            task_data = {}

            # Get task description
            task_data['task'] = task_match.group(2).strip() if task_match else sentence.strip()

            # Assign appropriate name if detected, otherwise "Unknown"
            task_data['person'] = "Unknown"
            for person in person_matches:
                # Check if person appears before the task in the sentence
                if sentence.index(person) < sentence.index(task_match.group(0)):
                    task_data['person'] = person
                    break

            # Extract deadline if present
            deadline_match = re.search(DEADLINE_PATTERN, sentence, re.IGNORECASE)
            task_data['deadline'] = deadline_match.group(2).strip() if deadline_match else "N/A"

            task_data['category'] = categorize_task(task_data['task'])
            # Add task to the list
            tasks.append(task_data)

    return tasks

# Categorize task based on keywords

def categorize_task(task):
    task_lower = task.lower()
    if any(word in task_lower for word in ['buy', 'purchase', 'get']):
        return 'Shopping'
    elif any(word in task_lower for word in ['review', 'read', 'check']):
        return 'Review'
    elif any(word in task_lower for word in ['submit', 'complete', 'send']):
        return 'Submission'
    elif any(word in task_lower for word in ['call', 'meet', 'attend']):
        return 'Meeting'
    else:
        return 'General'
