# Create your checklist
checklist = []
completed_tasks = []
incomplete_tasks = []

n = int(input("Number of tasks to be completed today: "))
for i in range(n):
    task = input(f"Enter task {i+1}: ")
    checklist.append(task)

print("\nChecklist for the day:")
for task in checklist:
    print("-", task)

print("\nAt the end of the day, answer with 'yes' or 'no' for each task:")

for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ").strip().lower()
    if status == 'yes':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\nCompleted Tasks:")
for task in completed_tasks:
    print("", task)

print("\nIncomplete Tasks:")
for task in incomplete_tasks:
    print("", task)
