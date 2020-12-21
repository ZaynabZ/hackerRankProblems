#All sorted lowercase letters are ahead of uppercase letters.
#All sorted uppercase letters are ahead of digits.
#All sorted odd digits are ahead of sorted even digits.
import re
word = "Sorting1243"
low = []
high = []
num = []
for c in word:
    if c.islower():
        low.append(c)
    elif c.isupper():
        high.append(c)
    elif c.isalnum():
        num.append(int(c))

num.sort(key=lambda x: (-(x % 2), x))

word = [*sorted(low), *sorted(high), *str(''.join(map(str, num)))]

print(''.join(word))

