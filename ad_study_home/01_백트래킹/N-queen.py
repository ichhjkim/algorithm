def tracking(count):
    global result
    if count == N:
        # print(height, '높이')
        # print(width, '가로')
        # print(cross_left, '왼쪽 대각선')
        # print(cross_right, '오른쪽 대각선')
        result += 1
    else:
        for i in range(N):
            if count not in height and (i-count not in cross_left) and (i+count not in cross_right) and i not in width:
                making(count, i)

                tracking(count+1)
                origin()

def making(count, i):

    height.append(count)
    width.append(i)
    cross_left.append(i-count)
    cross_right.append(i+count)

def origin():

    height.pop()
    width.pop()
    cross_right.pop()
    cross_left.pop()



N = int(input())

board = [[0]*N for _ in range(N)]
# print(board)
result = 0
width = []
height = []
cross_left = []
cross_right = []
tracking(0)
print(result)
