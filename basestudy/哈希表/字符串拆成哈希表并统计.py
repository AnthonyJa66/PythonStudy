from collections import Counter

s="yf g ghgh,hbf k"

de_map=set(s)
# print(de_map)
# list1=list(de_map)
# print(list1)
# list2=list(s)
# print(list2)

char_map=Counter(s)
most_common_char, count = max(char_map.items(), key=lambda x: x[1])
print(most_common_char, count)

print(char_map)
print(max(char_map.values()))
