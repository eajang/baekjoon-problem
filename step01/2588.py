A = int(input())
B = int(input())

B_100 = int(B / 100)
B_10 = int((B - (B_100 * 100)) / 10)
B_1 = int(B - (B_100 * 100) - (B_10 * 10))

E1 = A * B_1
E2 = A * B_10
E3 = A * B_100

print(E1)
print(E2)
print(E3)
print(E1 + (E2 * 10) + (E3 * 100))
