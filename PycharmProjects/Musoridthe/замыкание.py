def func1(param1):
    res_sum = 0  # Локальная переменная
    print("before:", res_sum)

    def func2(param2):
        nonlocal res_sum  # Ссылаемся на переменную из func1
        res = param1 + param2
        res_sum = res
        return res_sum

    return func2


call = func1(2)

print("Result:", call(3))  # Вывод результата
