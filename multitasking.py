import multitasking
import time

@multitasking.task  # <-- use multitasking.task
def fetch_data(url_id):
    # Simulate API call or I/O operation
    time.sleep(1)
    print(f"Data from {url_id}")  # better to print inside task

# These run concurrently, not sequentially!
for i in range(5):
    fetch_data(i)

# Wait for all tasks to complete
multitasking.wait_for_tasks()  # <-- prefix with multitasking

print("All data fetched!")
