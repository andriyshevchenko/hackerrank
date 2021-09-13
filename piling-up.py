# Enter your code here. Read input from STDIN. Print output to STDOU
import array

def test_case():
    return {
        'n': int(input()),
        'blocks': list(map(int, input().strip().split()))
    }

def execute(test_case: dict):
    n = test_case.get('n')
    blocks = array.array('l')
    blocks.fromlist(test_case.get('blocks'))
    
    pile = []
    
    leftmost = 0
    rightmost = n-1
    
    canBuild = True
    while len(pile) <= n:
        max_of_blocks: int
        min_of_blocks: int
        
        if blocks[leftmost] > blocks[rightmost]:
            max_of_blocks = leftmost
            min_of_blocks = rightmost
        else:
            min_of_blocks = leftmost
            max_of_blocks = rightmost
        if len(pile) == 0:
            pile.append(blocks[max_of_blocks])
            if max_of_blocks == rightmost:
                rightmost -= 1
            else:
                leftmost += 1
        else:
            last = pile.pop()
            pile.append(last)
        
            if last >= blocks[max_of_blocks]:
                pile.append(blocks[max_of_blocks])
                if max_of_blocks == rightmost:
                    rightmost -= 1
                else:
                    leftmost += 1
            elif last >= blocks[min_of_blocks]:
                pile.append(blocks[min_of_blocks])
                if min_of_blocks == rightmost:
                    rightmost -= 1
                else:
                    leftmost += 1
            else:
                #print('Break')                
                canBuild = False
                break
        #print([blocks[min_of_blocks], blocks[max_of_blocks], pile])
                
    if canBuild: 
        print('Yes')
    else:
        print('No')
        
T = int(input())

for i in range(T): execute(test_case())
