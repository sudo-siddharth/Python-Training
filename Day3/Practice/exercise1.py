reviews = [ "Great product! I loved it. Contact me at john.doe@example.com for details.",
   "Terrible service. I want a refund! My order number is 12345.",
   "Awesome quality. Will buy again. Email me: jane_smith22@gmail.com",
   "Poor packaging. Received a broken item. Invoice ID: 67890."]

#extracting email address from reviews
import re
print("\nextracting email address from reviews:\n")
for review in reviews:
    email = re.search(r'[\w\.-]+@[\w\.-]+', review)
    if email:
        print(email.group())

#checking if review contains a specific keyword
print("\nchecking if review contains a specific keyword:\n")
for review in reviews:
    if re.search("refund|broken", review):
        print(review)

#spliting review based on punctuations
print("\nsplitting reviews based on punctuations:\n")
for review in reviews:
    print(re.split(r'[.,!:]', review))

#replacing all numbers with "[Num]" using sub
print("\nreplacing all numbers with '[Num]' using sub:\n")
for review in reviews:
    print(re.sub(r'\d+', '[Num]', review))
