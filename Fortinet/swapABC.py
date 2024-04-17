# 给一个String最多只包含abc三种字母。其中相邻的a和b可以互换，b和c相邻可以互换。求互换后最小的string。
# Example: "bbbaacb"换完后最小是"aabbbbc"
import collections

def swapABC(s):
    n = len(s)
    firstC = -1
    for i in range(n):
        if s[i] == "c":
            firstC = i
            break
    if firstC == -1:
        retA = ""
        retB = ""
        for c in s:
            if c == "a":
                retA += c
            else:
                retB += c
        return retA+retB
    ret = ""
    cntB = 0
    for c in s:
        if c == "b":
            cntB += 1
    for i in range(firstC):
        if s[i] == "a":
            ret += "a"
    for i in range(cntB):
        ret += "b"
    for i in range(firstC, n):
        if s[i] != "b":
            ret += s[i]
    return ret

def swapABC2(s):
    ret = ''
    cnt = collections.Counter()

    for ch in s:
        if ch == 'a' and cnt['c'] > 0:
            ret += 'a' * cnt['a'] + 'b' * cnt['b'] + 'c' * cnt['c']
            cnt = collections.Counter()
        cnt[ch] += 1
    ret += 'a' * cnt['a'] + 'b' * cnt['b'] + 'c' * cnt['c']
    return ret

print(swapABC("bbbaacb"))
print(swapABC("bbacbca"))
print(swapABC("abaacacaac"))
print(swapABC("bbacbcabca"))

# print(swapABC2("bbbaacb"))
# print(swapABC2("bbacbca"))
# print(swapABC2("abaacacaac"))
# print(swapABC2("bbacbcabca"))

