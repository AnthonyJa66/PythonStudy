lst = [1, 2, 3]

# append 是将整个列表作为一个元素塞进去
lst.append([4, 5])
print(lst)  # 输出：[1, 2, 3, [4, 5]]  （长度变成4）

lst2 = [1, 2, 3]
# extend 是把里面的元素拆开追加
lst2.extend([4, 5])
print(lst2)  # 输出：[1, 2, 3, 4, 5]  （长度变成5）

lst = [10, 20, 30, 20]

# pop 按索引删（删掉索引为1的元素20，并返回它）
removed = lst.pop(1)
print(removed)  # 输出：20
print(lst)      # 输出：[10, 30, 20]

# remove 按值删（删掉第一个匹配的20）
lst.remove(20)
print(lst)      # 输出：[10, 30]  （注意：删的是原来的30后面的那个20，因为前面的20已经被pop删了）

nums = [3, 1, 4, 1, 5]

# 正序排序（默认）
nums.sort()
print(nums)  # 输出：[1, 1, 3, 4, 5]

# 倒序排序
nums.sort(reverse=True)
print(nums)  # 输出：[5, 4, 3, 1, 1]

# 反转（倒序排列，不是排序）
nums.reverse()
print(nums)  # 输出：[1, 1, 3, 4, 5]（又反回来了）