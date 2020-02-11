
def solution(brown, red):
    answer = []
    # 전체 갯수 - 겉에 갯수 > red
    allNum = brown + red
    for i in range(allNum, int(allNum**(1/2))-1, -1):
        if not allNum % i:
            width = i
            height = allNum // i
            t = 2*width + 2*(height-2)
            if allNum - t >= red:

                return [width, height]