# Жадібний продавець!

coin_publisher = (25, 10, 5, 1)
coins = 0
print('O hai! How much change is owed?')
amount = float(input()) * 100

for x in coin_publisher:
    coins += amount // x
    amount -= amount // x * x

print(int(coins))
