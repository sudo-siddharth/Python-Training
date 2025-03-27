print("Enter words seperated by hyphen (-)")
words = input().split('-')
print('-'.join(sorted(words)))