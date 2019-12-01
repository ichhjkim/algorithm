import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    fir = input()
    sec = input()

    fir_back = sec_back = len(fir)-1

    while sec_back < len(sec)-1 and fir_back > 0:

        if fir[fir_back] == sec[sec_back]:
            fir_back -= 1
            sec_back -= 1
        elif sec[sec_back] in fir:
            sec_back += len(fir)-1 - fir.index(sec[sec_back])
            fir_back = len(fir)-1
        else:
            fir_back = len(fir)-1
            sec_back += len(fir)

    
    if not fir_back:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))


    

