"""
字符串、列表、元组
"""

arr = [1, 2, 3, 4, 5, 16, 6, 7, -3, 8, 9]

print(len(arr))

print(sum(arr))

del arr[3]

print(arr)

print(max(arr))
print(min(arr))

arr2 = ["a", "b", "c", 4, 1]

print("d" in arr2)
print("c" in arr2)

print(arr + arr2)

print(arr2 * 3)

string1 = ["a", "b", 7]
string2 = ["a", "b", 5]
print(string1 > string2)