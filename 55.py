from collections import deque

def solution(play_time, adv_time, logs):
    result = ''
    play = 0
    play_time = play_time.split(':')
    for i in range(3):
        t = int(play_time[2-i])*(60**(i))
        play += t

    video = deque([0]*play)
    adv_time = adv_time.split(':')
    adv = 0
    loading = {}
    for i in range(3):
        t = int(adv_time[2-i]) * (60**(i))
        adv += t

    for l in range(len(logs)):
        startEnd = logs[l].split('-')
        start = startEnd[0].split(':')
        end = startEnd[1].split(':')
        s = e = 0
        for i in range(3):
            t = int(start[2 - i]) * (60 ** (i))
            s += t
        end = startEnd[1].split(':')
        for i in range(3):
            t = int(end[2 - i]) * (60 ** (i))
            e += t
        for time in range(s, e):
            if loading.get(time):
                loading[time] += 1
            else:
                loading[time] = 0

    max_result = 0
    for s in range(play):
        result = 0
        for ad in range(adv):
            if loading.get(s+ad):
                result += loading.get(s+ad)

        if result and result > max_result:
            max_result = result
    print(max_result)
    return max_result

solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])