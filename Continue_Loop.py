# Continue example: Skip a specific iteration
for num in range(1, 10):
    if num == 5:
        print("Skipping", num)
        continue
    print("Number:", num)
