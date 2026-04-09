n = 1
soma = 0

for d in range(1, 51):
    soma += n / d
    n += 2

print(f"O valor de S é: {soma:.2f}")