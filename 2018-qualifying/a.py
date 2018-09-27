
'''
Oversized Pan Flipper Problem

https://code.google.com/codejam/contest/3264486/dashboard#s=p0&a=1
'''

HAPPY_FACE = '+'
SAD_FACE = '-'


def pan_flips(sequence, flipper_size):
    flips = 0
    index = 0
    while((index + flipper_size) <= len(sequence)):
        if sequence[index] == SAD_FACE:
            for i in range(index, index + flipper_size):
                if sequence[i] == HAPPY_FACE:
                    sequence[i] = SAD_FACE
                else:
                    sequence[i] = HAPPY_FACE
            flips = flips + 1
        index = index + 1

    if any([x == SAD_FACE for x in sequence[index - 1:len(sequence)]]):
        return 'IMPOSSIBLE'

    return flips


t = int(input())
for i in range(1, t + 1):
    sequence, flipper_size = input().split(' ')

    flips = pan_flips(list(sequence), int(flipper_size))
    print('Case #%d: %s' % (i, flips))
