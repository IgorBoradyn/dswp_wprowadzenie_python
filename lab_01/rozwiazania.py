# Zad 1
int1 = int('10', 2)
int2 = int('71', 8)
float1 = float(2)
float2 = float('3.5')

print(int1)
print(int2)
print(float1)
print(float2)

# Zad 2
print(bin(int1), int1.bit_count())
print(bin(int2), int2.bit_count())
print(float1.is_integer())
print(float2.is_integer())

# Zad 3
print(int1 | int2)
print(int1 & int2)
print(int1 << 1)
print(int1 >> 1)
