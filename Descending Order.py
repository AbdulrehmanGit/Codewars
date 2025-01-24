# Description:
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    # Bust a move right here
    ns=  str(num)
    empty_list = []
    for i in ns:
        empty_list.append(int(i))
    x = sorted(empty_list)
    return int(''.join(map(str, x[::-1])))
