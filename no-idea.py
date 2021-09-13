# Enter your code here. Read input from STDIN. Print output to STDOUT
first_multiple_input = input().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

import array

arr = sorted(map(int, input().strip().split()))
A = sorted(map(int, input().strip().split()))
B = sorted(map(int, input().strip().split()))

data = array.array('l')
like = array.array('l')
dislike = array.array('l')

data.fromlist(arr)
like.fromlist(A)
dislike.fromlist(B)

i_data = 0
i_like = 0
i_dislike = 0
score = 0

while i_data < n:
    if i_like < m and data[i_data] == like[i_like]:        
        score += 1
        i_data += 1
    elif i_dislike < m and data[i_data] == dislike[i_dislike]:

        score -= 1
        i_data += 1
    else:
        cond1 = i_like < m and data[i_data] > like[i_like]
        cond2 = i_dislike < m and data[i_data] > dislike[i_dislike]
        if cond1:
            i_like += 1
        
        if cond2:
            i_dislike += 1
            
        if not cond1 and not cond2:
            i_data += 1
print(score)
