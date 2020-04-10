def solution(answer_sheet, sheets):

    max_result = 0
    print(answer_sheet)
    for i in range(len(sheets)):

        for j in range(i+1, len(sheets)):
            print(i, j)
            con = 0
            max_con = 0
            count = 0
            result = 0
            for x in range(len(answer_sheet)):
                #print(sheets[i][x], answer_sheet[x], sheets[j][x])
                if (sheets[i][x] != answer_sheet[x]) and (sheets[i][x]==sheets[j][x]):
                    count += 1
                    con += 1
                else:
                    max_con = max(max_con, con)
                    con = 0

        max_con = max(max_con, con)
        result = count + (max_con)**2
        print(count, max_con, result)
        max_result = max(max_result, result)

    return max_result