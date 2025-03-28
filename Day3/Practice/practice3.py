import os

if os.path.exists(r"Day3\Practice\textfile.txt"):
	with open(r"Day3\Practice\textfile.txt", "r") as f:
		content = f.read()
		print(content)
else:
    print("'textfile.txt' does not exist.")
	

# using os methods to remove the file
# os.remove(r"Day3\Practice\textfile.txt")

# using os methods to rename the file
os.rename(r"Day3\Practice\newfile.txt", r"Day3\Practice\textfile.txt")
print("File renamed successfully.")

#os simple walk method
for root, dirs, files in os.walk(r"Day3\Practice"):
    print(root)
    print(dirs)
    print(files)
    print("\n")

