# 모든 사무실은 호수로 구분
# 사무실은 여러층으로 나누어짐
# 직원 각자 지정된 자리를 1개 이상 사용
# 빈자리는 없음
# 한 사람이 한 사무실에서 지정된 자리 2개 이상 사용 안됨

# 해당 방에 이미 지정자리 있는 직원은 제외
# 지정 자리가 제일 적은 직원에게 우선순위
# 지정 자리 개수가 같으면 새 자리가 생긴 방에서 가장 자까운 방에 지정자리가 있는 직원이 우선순위가 더 높다
# 방과 방사이의 거ㅣ르는 호수와 소수의 절대값
# 여러 방을 가진 경우, 가지고 있는 방과 지정 자리 방과 가장 가까운 것을 기준
# 이름이 사전순으로 빠른 사람이 더 높은 순위

def solution(rooms, target):
    result = []
    people = {}
    for room in rooms:
        room = room.split(']')
        room_num = int(room[0][1:])
        pps = room[1].split(',')
        print(pps)
        for pp in pps:
            if people.get(pp):
                people[pp].append(room_num)
            else:
                people[pp] = [room_num]

    candidates = []
    for person, person_room in people.items():
        if target in person_room:
            continue
        else:
            min_t = 1000000
            for p_room in person_room:
                t = abs(target-p_room)
                if t < min_t: min_t = t
            candidates.append([[person, person_room, min_t]])

    candidates = sorted(candidates, key=lambda x: (len(x[1]), x[2] ,x[0]))
    result = [ candidate[0] for candidate in candidates]

    return result