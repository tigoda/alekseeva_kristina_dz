import random


def get_jokes(num):
    count = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for _ in range(num):
        joke = ' '.join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)])
        count.append(joke)
    return count


print(get_jokes(3))
