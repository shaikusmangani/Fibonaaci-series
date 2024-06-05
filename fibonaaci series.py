def fibonacci_series(n):
    series = [0, 1]
    if n <= 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return series  
    else:
        for i in range(2, n):
            next_term = fib_series[-1] + fib_series[-2]
            fib_series.append(next_term)
        return series


print(fibonacci_series(5))

  
