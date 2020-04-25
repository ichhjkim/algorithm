import re
def solution(registered_list, new_id):
    answer = ''
    if len(new_id) >= 3 and len(new_id) <= 6:
        pass
    else:
        return answer
    t = re.compile('[a-z0-9]')
    m = t.match(new_id)
    string_id = re.findall('[a-z]', new_id)
    int_id = re.findall('[0-9]', new_id)
    string_id = ''.join(string_id)
    if int_id:
        int_id = ''.join(int_id)
        if int_id[0] == '0':
            return answer
    else:
        int_id = ''

    if string_id+int_id != new_id:
        return answer

    if new_id not in registered_list:
        answer = new_id
        return answer
    else:
        if int_id:
            int_id = int(int_id)-1
        else: int_id = 0
        while True:
            int_id += 1

            t = string_id+str(int_id)
            if t not in registered_list:
                answer = t
                return answer

    return answer

print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))