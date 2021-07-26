"""Problem statement:
An anagram is a word whose characters can be rearranged to create another word. Given two strings
determine the minimum number of character in either string that must be modified to make the two 
strings anagram. If it is not possible to make the two strings anagram, return -1

Eg:
a = ["tea", "tea", "act"]
b = ["ate", "toe", "acts"]
"""


def getMinimumDifference(a, b):
    if len(a) != len(b):
        return -1
    answer = [-1 for _ in range(len(a))]
    for i in range(len(a)):
        wordA = list(a[i])
        wordB = list(b[i])
        wordA.sort()
        wordB.sort()
        if wordA == wordB:
            answer[i] = 0
        elif len(a[i]) != len(b[i]):
            continue
        else:
            answer[i] = countDiff(wordA, wordB)

    return answer


def countDiff(wordA, wordB):
    count = 0
    chars = {}
    for c in wordA:
        chars[c] = chars.get(c, 0) + 1
    for c in wordB:
        if c in chars:
            chars[c] -= 1
        else:
            count += 1
    return count


if __name__ == "__main__":
    a1 = ["tea", "tea", "act"]
    b1 = ["ate", "toe", "acts"]
    a2 = ["a", "jk", "abb", "mn", "abc"]
    b2 = ["bb", "kj", "bbc", "op", "def"]
    print(getMinimumDifference(a1, b1))  # [0,1,-1]
    print(getMinimumDifference(a2, b2))  # [-1,0,1,2,3]
