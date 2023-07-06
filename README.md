# read_and_write_in_Python
Exercise to read from and write to files in Python

Certainly! Here's a simple exercise that will help you practice reading and writing files in Python:
Exercise:
1. Create a new text file called "guests.txt" and write the names of three guests in separate lines.
   For example, the contents of "guests.txt" could be:

```
   John
   Sarah
   Michael
```
2. Write a Python program that reads the contents of the "guests.txt" file and displays them on the console.
3. Append the name of a new guest to the end of the "guests.txt" file using your Python program. For example, you can add the name "Emily".
4. Verify that the new guest's name has been appended to the "guests.txt" file by reading its contents and displaying them on the console again.
Here's a possible solution:

```
# Step 2: Read and display the contents of the file
with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Step 3: Append a new guest's name to the file
new_guest = "Emily"
with open("guests.txt", "a") as file:
    file.write("\n" + new_guest)  # add newline before appending

# Step 4: Read and display the updated contents of the file
with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip())

```

When you run this program, it should display the names of the three initial guests on the console, append the name "Emily" to the file, and then display the updated list of guests.

<img src="image/read_write_image.png">