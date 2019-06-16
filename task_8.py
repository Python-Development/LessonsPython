# Пірамідка Маріо - 2

height = 8
print('height', height)
for i in range(height):
    x = height - i
    for j in range(i * 2 + 4):
        print('#'.rjust(x), end='')
        x = 0
    print('')
