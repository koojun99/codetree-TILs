def generate_sequences(k, n, sequence=[], result=[]):
    if len(sequence) == n:
        result.append(tuple(sequence))
        return
    for i in range(1, k + 1):
        if len(sequence) < 2 or (sequence[-1] != i or sequence[-2] != i):
            generate_sequences(k, n, sequence + [i], result)

k, n = map(int, input().split())
result = []
generate_sequences(k, n, [], result)

for seq in result:
    print(' '.join(map(str, seq)))