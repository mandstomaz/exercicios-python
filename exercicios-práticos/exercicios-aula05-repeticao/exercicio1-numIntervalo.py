int1 = 0
int2 = 0
int3 = 0
int4 = 0

num = int(input("Digite um número: "))

while num >= 0:
    if num <= 25:
        int1 += 1
    else:
        if num <= 50:
            int2 += 1
        else:
            if num <= 75:
                int3 += 1
            else:
                if num <= 100:
                    int4 += 1
    num = int(input("Digite um número: "))

print(f"0 - 25: {int1}")
print(f"26 - 50: {int2}")
print(f"51 - 75: {int3}")
print(f"76 - 100: {int4}")