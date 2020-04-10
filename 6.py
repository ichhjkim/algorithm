def solution(directory, command):

    for d in range(len(directory)):
        directory[d] = directory[d].split('/')
        directory[d] = directory[d][1:]

    for co in command:
        co = co.split(' ')
        if co[0] == "mkdir":
            co[1] = co[1].split('/')
            co[1] = co[1][1:]
            directory.append(co[1])

        if co[0] == "cp":

            co[1] = co[1].split('/')
            co[1] = co[1][1:]

            co[2] = co[2].split('/')
            co[2] = co[2][1:]

            directory.append(co[2]+co[1])

        if co[0] =="rm":
            co[1] = co[1].split('/')
            co[1] = co[1][1:]
            for i in range(len(directory)):
                for c in range(len(co[1])):
                    if co[1][c] == directory[i][c]:
                        pass
                    else:
                        break
            else:
                directory.pop(i)

    for d in range(len(directory)):
        directory[d] = '/'.join(directory[d])
        directory[d] = '/'+directory[d]
        print(directory[d])
    directory.sort()
    answer = []
    return directory
a = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
b = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]
print(solution(a, b))