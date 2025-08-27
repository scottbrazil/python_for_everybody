# ^ Matches the beginning of a line
# $ Matches the end of the line
# . Matches any character
# \s Matches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy)
# + Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (Indicates where string extraction is to start
# ) Indicates where string extraction is to end

import re

#s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#l = re.findall('\S+?@\S+', s)
#print(l)
total = 0
with open('regex_sum_2285824.txt', 'r') as f:
    for line in f:
        lst = re.findall('[0-9]+', line.strip())
        if len(lst) > 0:
            int_lst = [int(x) for x in lst]
            total = total + sum(int_lst)
print(total)

total = 0
with open('regex_sum_42.txt', 'r') as f:
    for line in f:
        lst = re.findall('[0-9]+', line.strip())
        if len(lst) > 0:
            for n in lst:
                total = total + int(n)
print(total)

