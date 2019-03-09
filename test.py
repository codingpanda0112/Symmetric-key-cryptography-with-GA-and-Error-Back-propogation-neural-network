s = '12345678909'
print(list(map(''.join, zip(*[iter(s)]*2))))
