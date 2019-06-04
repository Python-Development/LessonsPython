# Пірамідка Маріо

stepsOfThePyramid = (
    '##',
    '###',
    '####',
    '#####',
    '######',
    '#######',
    '########',
    '#########'
)
print('height:', len(stepsOfThePyramid))

mario = 0

while mario != len(stepsOfThePyramid):
    print(stepsOfThePyramid[mario].rjust(9))
    mario += 1
