def probability(dice_number, sides, target):
    def rec(check, list2, c=0, x=0, y=0):
        list1 = []
        if check != 0:
            for i, p in enumerate(list2):
                if i < sides:
                    x += p
                    list1.insert(i, x)
                else:
                    y += list2[c]
                    x += p
                    list1.insert(i, x - y)
                    c += 1
            r = sides - 2
            for i in range(r + 1):
                list1.insert(len(list1), list1[r])
                r -= 1
            return rec(check - 1, list1)
        return round(list2[target - dice_number] / (sum(list2)), 4) \
            if sides * dice_number >= target >= dice_number else 0

    return rec(dice_number - 1, [1 for i in range(sides)])


print(probability(2, 6, 2))
