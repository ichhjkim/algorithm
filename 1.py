def solution(inputString):
    answer = 0
    stack = []

    for i in inputString:
        if i=='(' or i=='{' or i=='[' or i=='<':
            if i=='(':
                stack.append(')')
            elif i=='{':
                stack.append('}')
            elif i=='[':
                stack.append(']')
            elif i=='<':
                stack.append('>')

        elif i==')' or i=='}' or i==']' or i=='>':
            if stack:
                t = stack.pop()
            else:
                answer = -1
                break

            if t==i:
                answer += 1
            else:
                answer=-1
                break

        else: pass


    return answer