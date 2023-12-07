a = input("Введите строку: ")
b_count = {}
for c in a:
    if c in b_count:
        b_count[c] += 1
    else:
        b_count[c] = 1
print("Словарь:", b_count)