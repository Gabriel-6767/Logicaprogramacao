def gerar_fibonacci():
    a, b = 0, 1
    fibonacci_sequence = []

    while a <= 500:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

resultado = gerar_fibonacci()
print(resultado)
