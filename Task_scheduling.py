import schedule
import time
#define the task
def my_task():
    print("running my schedule task")

# Schedule the task to run every minute

schedule.every(2).minutes.do(my_task)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
