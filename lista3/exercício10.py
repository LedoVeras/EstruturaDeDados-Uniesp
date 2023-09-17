def fibonacci(n):
    fib_seq = []
    prev_fibo, fibo = 0, 1
    for _ in range(n):
        fib_seq.append(prev_fibo)
        prev_fibo, fibo = fibo, prev_fibo + fibo
    return fib_seq

n = int(input("digite o número de termos desejados de fibonacci: "))

print(f'fibonacci com {n} termos: {fibonacci(n)}')
