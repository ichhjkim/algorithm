def solution(answer_sheet, sheets):
    stu = len(sheets)
    ans_size = len(answer_sheet)
    max_result = 0
    for i in range(stu):
        for j in range(stu):
            count = 0
            con = 0
            max_con = 0
            if i < j:
                print(sheets[i], sheets[j])
                for s in range(ans_size):

                    if sheets[i][s] == answer_sheet[s]:
                        max_con = max(max_con, con)
                        con = 0
                    else:
                        if sheets[i][s] == sheets[j][s]:
                            print(sheets[i][s], sheets[j][s])
                            count += 1
                            con += 1
                        else:
                            max_con = max(max_con, con)
                            con = 0

                max_con = max(max_con, con)
                result = count + (max_con**2)
                max_result = max(max_result, result)
    return max_result


print(solution("24551", ["24553", "24553", "24553", "24553"]))
