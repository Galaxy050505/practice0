n = int(input())
for i in range(1, n + 1):
    a = abs(i - (n + 1) // 2)
    print(" " * a + "*" * (n - 2 * a) + " " * a)