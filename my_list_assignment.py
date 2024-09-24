# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append the elements 10, 20, 30, and 40 to my_list
my_list.append(10)  # Appending 10
my_list.append(20)  # Appending 20
my_list.append(30)  # Appending 30
my_list.append(40)  # Appending 40

# Step 3: Insert the value 15 at the second position in the list
# Indexing starts at 0, so index 1 is the second position
my_list.insert(1, 15)

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])  # Adding multiple elements at once

# Step 5: Remove the last element from my_list
# The pop() function removes and returns the last element by default
my_list.pop()

# Step 6: Sort my_list in ascending order
my_list.sort()  # Sorting the list in-place in ascending order

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)  # Finding the index of the value 30
print(f"The index of 30 in my_list is: {index_of_30}")

# Print the final list after all operations
print("Final my_list:", my_list)
