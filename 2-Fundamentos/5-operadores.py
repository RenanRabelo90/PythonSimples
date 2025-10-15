num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

#Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"a soma de: {num1} + {num2} é igual a {sum}")
print(f"a subtração de: {num1} - {num2} é igual a {sub}")
print(f"a divisão de: {num1} / {num2} é igual a {div}")
print(f"a multiplicação de: {num1} * {num2} é igual a {mult}")
print(f"o resto da divisão de: {num1} / {num2} é igual a {mod}")
print(f"{num1} elevado a {num2} é igual a {exp}")

#Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(bigger)
print(smaller)
print(equal)
print(different)
print(bigger_equal)
print(smaller_equal)

print(f"O número {num1} é maior que o número {num2}? {bigger}")
print(f"O número {num1} é menor que o número {num2}? {smaller}")
print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"Os números {num1} e {num2} são diferentes? {different}")
print(f"O número {num1} é maior ou igual ao número {num2}? {bigger_equal}")
print(f"O número {num1} é menor ou igual ao número {num2}? {smaller_equal} ")

# Atribuição
num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1