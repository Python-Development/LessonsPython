print('"Hello, World!"')

step = '#'
height = 0

print('height: 8')
while height != 8:
    for i in range(8):
        step += '#'
        print(step.rjust(9) + step.ljust(9))
        height += 1

