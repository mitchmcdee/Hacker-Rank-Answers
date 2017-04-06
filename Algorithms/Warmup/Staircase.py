n = int(input().strip())

[print("{0}{1}".format(" " * ((n - i) - 1), "#" * (i + 1))) for i in range(n)]