# Open and read content from file
with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes newline characters
        
# Append "Emily" to the file

new_guest = "Emily"

with open("guests.txt", "a") as file:
    file.write("\n" + new_guest) # add newline before appending

with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip())

