## Welcome to my enumerate() practice log

fruits = ["apple", "banana", "cherry"]
for index, fuit in enumerate(fruits):
    print(index, fruit)


tasks = ["drink water", "read a book", "do homework", "rest"]

print("Tasks that inclue the word 'homework':\n")


for index, task in enumerate(tasks, 1):
    if "homework" in task:
        print(f"{index}. {task}")

        # practicing \n    move to the new line
print("Hello\nWorld")

name = "Christin"
instrument = "Cello"

print("Name:", name, "n\Instrument:", instrument)

print("Tasks:\n- Work\n- Practice\n- Eat\n- Sleep\n- Code")

print("Enter your task(type 'done' to finish):")

tasks = []

while True:
    task = input("- ")
    if task.lower() == "done":
        breaktasks.append(task)

print("\n Your Task List:\n")

for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")


name = "Christin"
print(f"My name is {name}")

for i, t in enumerate(tasks, 1):
    if t["days_left"] < 0:
        status = "❗ OVERDUE"
    elif t["days_left"] == 0:
        status = "🔥 DUE TODAY"
    else:
        status = f"⏳ In {t['days_left']} day(s)"

    formatted_due = t["due_date"].strftime("%a %b %d")
    print(f"{i}. {t['task']:<30} | {formatted_due} | {status}")

# Using enumerate(tasks, 1) to get both index (i) and each task (t)
#    - Starts counting from 1 for cleaner output

# Used index i to number each task in the printed list

# Used f-string with formatting:
#    - {i}. for numbering
#    - {t['task']:<30} for left-aligning task name to make the output look clean
#    - status messages (🔥, ❗, ⏳) based on days_left

# Combined enumerate + conditional logic + string formatting → neat CLI output!
