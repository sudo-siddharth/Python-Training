
words = ["Hello", "world", "Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence) 


items = ["apple", "banana", "cherry"]
csv = ",".join(items)
print(csv) 


paths = ["home", "user", "documents", "file.txt"]
file_path = "/".join(paths)
print(file_path)


numbers = [1, 2, 3, 4, 5]
number_string = "-".join(map(str, numbers))
print(number_string)