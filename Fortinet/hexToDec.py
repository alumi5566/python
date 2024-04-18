# convert base 16 variables into 10 based variables，
# Input : 67 Output: 103
#
# Input : 512 Output: 1298
#
# Input : 123 Output: 291

def convert(hex):
    base = 16
    p = 0
    ret = 0
    for i in range(len(hex)-1, -1, -1):
        if "0" <= hex[i] <= "9":
            ret += ( ord(hex[i])-ord("0") ) * pow(base, p)
        elif "a" <= hex[i] <= "f":
            ret += ( ord(hex[i])-ord("a") ) * pow(base, p)
        p += 1
    # return ret
    return str(ret)

print(convert("67"))
print(convert("512"))
print(convert("123"))