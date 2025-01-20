# Description:
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(st):
    result = []
    for i in range(len(st)):
        # Capitalize the first letter and lowercase the rest
        formatted = st[i].upper() + st[i].lower() * i
        result.append(formatted)
    return '-'.join(result)
