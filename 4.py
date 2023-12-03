def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum

n = int(input("Введите число n: "))
result = sum_of_squares(n)
print("Сумма квадратов всех чисел от 1 до", n, "равна", result)
