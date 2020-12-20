# Pair socks by colors
# The program returns the number of pairs of socks of the same color that can be matched
# This solution is correct but of o(n^2) zhich makes it wrong


def sockMerchant(n, ar):
    pairs = 0
    for item in set(ar):
        pairs += ar.count(item) // 2

    return pairs


n = int(input())
ar = list(map(int, input().rstrip().split()))

print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))

