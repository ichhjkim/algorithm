from collections import deque


def solution(food_times, k):
    answer = 0
    queue = deque([0] * len(food_times))
    for i in range(len(food_times)):
        queue[i] = [food_times[i], i + 1]

    time = 0
    while queue:

        if time == k:
            answer = queue[0][1]
            print(answer)
            return answer

        temp = queue.popleft()
        temp[0] -= 1
        if temp[0] > 0: queue.append(temp)

        time += 1

    return -1


from collections import deque


def solution(food_times, k):
    answer = 0
    queue = deque([0] * len(food_times))
    for i in range(len(food_times)):
        queue[i] = [food_times[i], i + 1]

    time = 0
    while queue:

        if time == k:
            answer = queue[0][1]
            print(answer)
            return answer

        temp = queue.popleft()
        temp[0] -= 1
        if temp[0] > 0: queue.append(temp)

        time += 1

    return -1


def solution1(food_times, k):
    queue = list(range(1, len(food_times) + 1))

    index = 0
    time = 0
    while queue:
        if time == k:
            answer = queue[index]
            return answer

        t = queue[index] - 1
        food_times[t] -= 1
        time += 1

        if food_times[t] <= 0:
            queue.pop(index)
            if index > len(queue)-1:
                index = 0
            continue

        if index == len(queue) - 1:
            index = 0
        else:
            index += 1

    return -1


solution1([3, 1, 2], 5)