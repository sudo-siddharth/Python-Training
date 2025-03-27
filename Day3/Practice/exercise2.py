import re

data = [
   "According to (Smith, 2020), the findings were groundbreaking.",
   "See reference [12] for more details. Also check (Doe & Johnson, 2018).",
   "Total cost: $129.99, but in Europe it’s €2500 and in India ₹1,50,000.",
   "Valid variables: my_var, _hiddenValue, data123, but 123wrong is invalid.",
   "Popular abbreviations: NASA, AI, FBI, OK, but 'ok' and 'abc' are not acronyms.",
   "Here's a simple code snippet: ```print('Hello, world!')```.",
   "Another code block: <code>def add(a, b): return a + b</code>",
   "IPv6 addresses to check: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, ::1",
   "I worked for 2h 30m yesterday. Today, I will work for 1d 12h straight!",
   "Some palindromes are: madam, racecar, refer, level, but hello is not one."
]

# extracting in format (author,year).And also fetching numbers like [12] if present
for i in data:
    references=re.findall(r'\([A-Za-z &]+,\s\d{4}\)|\[[0-9]+\]', i)
    if references:
        print(references)

# # finding all acronyms which are more than 3 letter long and are uppercase
for i in data:
    acronyms=re.findall(r'\b[A-Z]{3,}\b', i)
    if acronyms:
        print(acronyms)

# # finding all valid IPV6 addresses
for i in data:
    ip=re.findall(r'[0-9a-fA-F:]{3,}', i)
    if ip:
        print(ip)


# extracting time durations in format 2h 30m, 1d 12h
print("\nTime:\n")
for i in data:
    time = re.findall(r'\d+[hmd](?: \d+[hmd])*', i)
    if time:
        print(time)

# finding all palindromes
print("\nPalindromes:\n ")
for i in data:
    palindrome=re.findall(r'\b([a-zA-Z]+)\b', i)
    for j in palindrome:
        if len(j) > 1 and j == j[::-1]:
            print(j)
