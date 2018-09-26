# import collections
tidy_numbers = []
tidy_set = ()


def last_tidy(n):
    num = tidy_numbers[0]
    prev = num
    for i in range(1, len(tidy_numbers)):
        if n < num:
            return prev

        prev = num
        num = tidy_numbers[i]

    return 1


def generate_tidy_numbers(limit):
    num = 0
    index = 0
    while(True):
        for i in range(1, 10):
            if (i >= num % 10):
                tidy_numbers.append(num * 10 + i)
        num = tidy_numbers[index]
        index += 1
        if index > len(tidy_numbers) or num > limit:
            break


generate_tidy_numbers(pow(10, 18))
tidy_set = set(tidy_numbers)
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print('Case #%d: %d' % (i, last_tidy(n)))
