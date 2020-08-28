# 중간 딕셔너리 키
# 딕셔너리 2개
# 1개는 채팅 방 내용
# 1개는 닉네임 저장용
# 채팅 레코드
def solution(record):
    answer = []
    id = {}
    save = []
    for r in record:
        r = r.split(' ')
        if r[0] == "Enter":
            id[r[1]] = r[2]
            save.append([r[1], "님이 들어왔습니다."])
        elif r[0] == "Leave":save.append([r[1], "님이 나갔습니다."])
        elif r[0] == 'Change':id[r[1]] = r[2]

    result = [0] * len(save)
    for i in range(len(result)):result[i] = id[save[i][0]] + save[i][1]
    return result

print(
    solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
)