arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
arr = arr[len(arr) % 2:]

odd = [value for index, value in enumerate(arr) if not index % 2]
even = [value for index, value in enumerate(arr) if index % 2]

result = (
    prev if prev > current else current for prev, current in zip(odd, even)
)

print(list(result))  # [12, 44, 4, 10, 78, 123]
