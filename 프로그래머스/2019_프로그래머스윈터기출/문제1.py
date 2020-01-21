def solution(W, H):

    if W == H:
        print(W*H-W)
    elif W and H:
        a = min(W, H)
        b = max(W, H)
        if not a % 2:
            if not b % 2:
                return a*b-((b//a)*2)

            else:
                return a*b-(((b//a)+1)*2)
        else:
            if not b % 2:
                return a*b-(((b//a)+1)*2)
            else:
                return a*b-(((b//a)+1)*2+1)
    else:
        return 0