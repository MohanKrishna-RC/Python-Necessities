def longest_special_subseq(_n, dist, chars):
    chars = tuple(ord(char) - ord("a") for char in chars)
    print(chars)
    lengths = [0] * 26
    # print(lengths)
    for char in chars:
        c_from = max(char - dist, 0)
        c_to = min(char + dist, 25)
        longest = max(lengths[c_from: c_to+1])
        print(longest)
        lengths[char] = longest + 1

    return max(lengths)


t = int(input())
for tc in range(t):
    n, k, s = input().split()
    n = int(n)
    k = int(k)
    print(longest_special_subseq(n, k, s))
