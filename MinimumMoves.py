#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr1
#  2. INTEGER_ARRAY arr2
#
def minimumMoves(arr1, arr2):
    # Write your code here
    moves = 0
    
    for x in zip(map(str, arr1), map(str, arr2)):
        length = len(x[0])
        for i in range(length):
            moves += abs(int(x[0][i]) - int(x[1][i]))
    return moves