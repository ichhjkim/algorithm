change = 1000-int(input())

count = 0
while change:

    if change>= 500:
        change -= 500
        count += 1
    elif change >= 100:
        change -= 100
        count += 1
    elif change >= 50:
        change -= 50
        count += 1
    elif change >= 10:
        change -= 10
        count += 1
    elif change >= 5:
        change -= 5
        count += 1
    elif change >= 1:
        change -= 1
        count += 1

print(count)

