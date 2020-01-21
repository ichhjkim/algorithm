def permutation(depth, temp, visited, letter, N):
    global result
    if depth == N:
        result.append(temp)

    else:
        for i in range(len(visited)):
            if visited[i]:
                ori = temp
                temp += letter[i]
                visited[i] -= 1
                permutation(depth+1, temp, visited, letter, N)
                visited[i] += 1
                temp = ori


result = []
def anagrams(word, words):
    no_same = set(word)
    N = len(word)
    visited = [0]*len(no_same)
    letter = [0]*len(no_same)
    i = 0
    for n in no_same:
        t= word.count(n)
        visited[i] = t
        letter[i] = n
        i += 1
    permutation(0, '', visited, letter, N)
    anw = []
    for w in words:
        if len(w) == N:
            for r in result:
                if w == r and w not in anw:
                    anw.append(w)
    #print(anw)
    return anw
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])

