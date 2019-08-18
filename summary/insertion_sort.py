def insertion_sort(seq):
    
    for i in range(1, len(seq)):
        j = i
        
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        
    return seq
    

seq = [11, 3, 28, 43, 9, 4]

print(insertion_sort(seq))

def insertion_re(seq):

    for i in range(1, len(seq)):
        j = i

        while j > 0 and seq[j-1] < seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

    return seq

print(insertion_re(seq))