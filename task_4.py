# розрахунок депозиту при відомій
# Річній % ставці при щомісячному
# нарахуванні відсотків

deposit = int(input("Введіть суму вашого депозиту: "))
depositRate = int(input("Введіть % - річну ставку: "))

for month in range(1, 13):
    deposit = deposit * (100 + depositRate) / 100
    print("Ваш депозит на кінець ", month, " місяця складає: ", ("%.2f" % deposit))
