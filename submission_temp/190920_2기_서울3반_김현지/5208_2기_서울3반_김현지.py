T= int(input())

def bus(energy, recent):
    global min_count
    global count
    # print(recent, '현재위치')
    ori_energy = energy
    if recent >= nums[0]:
        return
    if recent+energy >= nums[0]:
        if count < min_count:
            min_count = count

    else:
        for e in range(1, energy+1):
            energy -= 1
            energy = battery[recent+e]
            if count + 1 < min_count:
                count += 1
                bus(energy, recent+e)
                count -= 1
            energy = ori_energy

for tc in range(1, T+1):

    nums = list(map(int, input().split()))
    # 정류장 1부터로 하기 위해
    stations = [0]*(nums[0]+1)
    # stations 마지막 인덱스에는 배터리가 없뜸, station과 인덱스를 맞추기 위해
    battery = [0] + nums[1:]+[0]
    # 충전횟수, 처음 충전은 제외
    count = 0
    # 최소 충전
    min_count = 10000000000000000
    # 정류장 1번의 충전지는 넣고 시작
    energy = battery[1]
    # 지금 위치
    recent = 1
    bus(energy, recent)

    print('#{} {}'.format(tc, min_count))