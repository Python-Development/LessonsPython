# Пірамідка Маріо 2

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
    print(stepsOfThePyramid[mario].rjust(9),
          stepsOfThePyramid[mario].ljust(9))
    mario += 1
