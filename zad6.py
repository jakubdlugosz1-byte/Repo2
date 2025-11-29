def merge_and_cube(list1: list, list2: list) -> list:
    merged = list1 + list2
    unique = list(set(merged))
    cubed = [x ** 3 for x in unique]
    return cubed

a = [1, 2, 3, 3]
b = [3, 4, 5]

result = merge_and_cube(a, b)
print(result)
