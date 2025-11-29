def list_contains_value(values: list, value: int) -> bool:
    return value in values

nums = [1, 2, 3, 4, 5]
result = list_contains_value(nums, 3)
print("Czy lista zawiera 3?", result)
