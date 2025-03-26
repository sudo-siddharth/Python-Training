for i in range(1,50):

    if i == 40:
        break
    elif i%3 == 0:
        pass

    elif i%5 == 0:
        continue
    else:
        print("Processing", i)