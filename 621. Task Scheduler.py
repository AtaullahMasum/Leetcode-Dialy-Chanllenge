
#1. Count the frequency of each task and find the task with the maximum frequency.
#2. Calculate the total number of slots required for all tasks without considering the cooling period.
#3. Calculate the number of idle slots required based on the task with the maximum frequency.
#4. Add the idle slots to the total number of slots.
#5. Return the maximum of the total number of slots and the length of the input tasks list.

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Find the task with the maximum frequency
        max_freq = max(task_counts.values())
        
        # Calculate the total number of slots required for all tasks
        total_slots = (max_freq - 1) * (n + 1)
        
        # Calculate the number of tasks that have the same maximum frequency
        max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Add the tasks with the maximum frequency to the total slots
        total_slots += max_freq_tasks
        
        # Return the maximum of the total slots and the length of the tasks list
        return max(total_slots, len(tasks))