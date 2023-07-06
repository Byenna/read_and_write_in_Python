# Open and read content from file
with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes newline characters
        