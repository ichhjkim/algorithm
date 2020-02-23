goods = [[3100, 2], [7700, 1], [3100, 2]]
coupons = [[33, 4]]

goods = sorted(goods, reverse=True)

coupons = sorted(coupons, reverse=True)

def working():
    result = 0

    for i in range(len(coupons)):

        while coupons[i][1]:

            for j in range(len(goods)):
                while goods[j][1]:
                    goods[j][1] -=1
                    coupons[i][1] -= 1
                    result += goods[j][0]*(100-coupons[i][0])*(1/100)
                    if not coupons[i][1]: break
                if not coupons[i][1]: break
            else:
                return result


    for x in range(len(goods)):
        if goods[x][1]:
            result += goods[x][0]
    return result




print(int(working()))











