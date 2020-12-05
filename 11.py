import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    parse = re.sub(r'[~!@#$%^&*()=+[{}:/?,<>]', '', new_id)
    parse = parse.replace(']', '')
    parse = re.sub('\.{2,}', '.', parse)

    if parse and parse[0] == '.':
        parse = parse[1:]
    if parse and parse[-1] == '.':
        parse = parse[:-1]

    if parse == '' : parse = 'a'

    if len(parse) >= 16:
        parse = parse[:15]
        if parse[-1] == '.':
            parse = parse[:-1]
    if len(parse) <= 2:
        while True:
            parse = parse + parse[-1]
            if len(parse) == 3:
                return parse
    print(parse)
    return parse

solution("...!@BaT#*..y.abcdefghijklm"	)