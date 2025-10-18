import math

# 1 - Acessar o numero PI
print(f"{math.pi:.2f}")

# 2 - Acessar o número de euler
print(math.e)

# 3 - Arredondar
num = 10.4
print(math.ceil(num))
print(math.floor(num))

# 4 - Fatorial de um número
num2 = int(input("Digite um número:\n"))
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(5, 5))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC (máximo divisor comum)
mdc = math.gcd(50, 70)
print(mdc)

# 8 - Logaritmo
print(math.log(10))