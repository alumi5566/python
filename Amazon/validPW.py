# the variablility of password = number of password cna be obtained by reversing any substring from original passwrod
# ie. password = "abc"
# reverse any length 1 substring == original password "abc"
# reverse "ab" == "bac"
# reverse "bc" == "acb"
# reverse "abc" == "cba"
# the variablility is 4
# sample: "abaa" -> 4
import collections


# https://www.1point3acres.com/bbs/thread-1047238-1-1.html
# 一个字符串分割成子串的数量是固定的，即1+2+...+n，只要找到所有分割后是回文子串的数量，总数再减去回文数量，就找到能够通过翻转获得新串的子串数量。找回文子串可以用回溯，参考
# https://leetcode.com/problems/palindrome-partitioning/description/


def solution(password):
    c = collections.defaultdict(int)
    for p in password:
        c[p] += 1
    n = len(password)
    total = 1
    for v in c.values():
        total+=v*(n-v)
        n-=v
    return total
print(solution("abc"))
print(solution("abaa"))