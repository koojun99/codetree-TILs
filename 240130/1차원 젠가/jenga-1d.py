n = int(input())
numbers = [int(input()) for _ in range(n)]
end_of_array = n

def cut_array (start, end):
    global end_of_array,numbers

    temp_arr = []
    for i in range(end_of_array):
        if i < start or i > end:
            temp_arr.append(numbers[i])
    end_of_array = len(temp_arr)
    for i in range(end_of_array):
        numbers[i] = temp_arr[i]

for _ in range(2):
    start, end = tuple(map(int, input().split()))
    cut_array(start-1, end-1)

print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])