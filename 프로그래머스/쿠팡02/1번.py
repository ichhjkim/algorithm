def solution(rates, customers):
    answer = 0
    result = 0
    for customer in customers:
        ring = customer[0]*60
        msg = customer[1]
        data = customer[2]
        fare = 100000000000000000
        for rate in rates:
            t = 0
            t += rate[0]
            r = ((ring)-(rate[1]*60))*rate[2]
            if r > 0 : t += r
            m = (msg-rate[3])*rate[4]
            if m > 0 : t += m
            d = (data-rate[5])*rate[6]
            if d > 0 : t += d
            if fare > t:
                fare = t
        result += fare

    return result