def sum_of_squares(n):
    result = 0
    for i in range(n + 1):
        if i % 2 == 0:
            result += i ** 2
    return result

print(sum_of_squares(1000))
