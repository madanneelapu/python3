# creating random numbers generator
import random


def random_nums_gen():
    for v in range(1, 11):
        yield random.randint(100, 200)


def random_numbers_unique():
    cache = set()
    while len(cache) < 10:
        num = random.randint(100, 200)
        if num not in cache:
            cache.add(num)
            yield num


def random_nums_gen_with_count(count=10, start=100, end=200):
    for v in range(1, count + 1):
        yield random.randint(start, end)


# for n in random_nums_gen():
#     print(n)

# for n in random_nums_gen_with_count(start=500, end=600):
#     print(n)

for n in random_numbers_unique():
    print(n)