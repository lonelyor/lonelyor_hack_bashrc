import random

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sa = []

for i in range(8):
    sa.append(random.choice(seed))

result = ''.join(sa)
print(result)