'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из
трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
'''


from random import choice

def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    used = []
    joke = []
    for i in range(n):
        parts = [nouns, adverbs, adjectives]
        joke.clear()
        for i in parts:
            joke.append(choice(i))
        print(' '.join(joke))



get_jokes(2)
