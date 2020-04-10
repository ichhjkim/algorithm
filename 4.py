def solution(snapshots, transactions):
    ac = {}

    for snapshot in snapshots:
        ac.setdefault(snapshot[0], 0)
        ac[snapshot[0]] = int(snapshot[1])
    t= {}
    for transaction in transactions:
        ac.setdefault(transaction[2], 0)

        if t.get(transaction[0]): continue
        else: t.setdefault(transaction[0], 1)
        if transaction[1] == "SAVE":
            ac[transaction[2]] += int(transaction[3])
        elif transaction[1] == "WITHDRAW":
            ac[transaction[2]] -= int(transaction[3])

    answer = [[k, str(v)] for k, v in ac.items()]
    answer.sort()
    return answer

s= [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
]
a = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
print(solution(s, a))