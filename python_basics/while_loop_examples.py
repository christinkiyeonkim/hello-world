# while_loop_examples.py

# Example 1: Count from 1 to 5

print("Example 1: Count from 1 to 5")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

    print("------")

# Example 2: Ask user to type until they say 'exit'

print("Example 2: Type 'exit'to stop.")
user_input = ""
while user_input != "exit":
    user_input = input("Say something (type 'exit' to quit):")
    print("You said:", user_input)
print("Goodbye!")
