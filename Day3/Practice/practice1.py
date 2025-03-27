import re

# basic examples of regex with string in python
txt = "The rain is going to stop soon"

res = re.findall("rain", txt)
print(res)

res = re.search("^r", txt)
print(res)

res = re.search("soon$", txt)
print(res)

res = re.search("going.*soon", txt)
print(res.group())

res = re.search("going.*stop", txt)
print(res.group())

res = re.split(" ", txt)
print(res)

res = re.split(",", txt)
print(res.string)

res = re.sub("rain", "sun", txt)
print(res)

res = re.sub("soon", "later", txt)
print(res)

#from senetnce finding the first number with ataleast 2 digits
txt = "The rain is going to stop soon and the temperature is 25 degree celsius"
res = re.search("\d{2,}", txt)
print(res.group())