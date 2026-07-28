from collections import Counter

s="yf g hbf k"

char_map=Counter(s)

print(char_map)
print(max(char_map.values()))
