def is_even(number: int) -> bool:
    return number % 2 == 0

value = 0
result = is_even(value)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
