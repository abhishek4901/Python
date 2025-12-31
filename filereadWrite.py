try:
    # Try to open and read the file
    with open("data.txt", "r") as f:
        print("File Content:")
        print(f.read())

except FileNotFoundError:
    # File does not exist
    print("File does not exist.")

    # Create new file and write data
    with open("data.txt", "w") as f:
        f.write("This file is created because it did not exist.")
    
    print("New file created and data written successfully.")
