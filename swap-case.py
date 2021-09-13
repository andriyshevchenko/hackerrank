def swap_case(s):
    return ''.join(map(compare, s))

def compare(c):
    if ord('a') <= ord(c) <= ord('z'):
        return chr(ord(c) + ord('A') - ord('a'))
    elif ord('A') <= ord(c) <= ord('Z'):
        return chr(ord(c) - ord('A') + ord('a'))
    else: return c
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)