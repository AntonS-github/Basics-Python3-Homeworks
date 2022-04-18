'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''
import random
def get_jokes(jokes_quantity):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    while jokes_quantity > 0:
        choose_nouns = ''.join(random.choices(nouns))
        choose_adverbs = ''.join(random.choices(adverbs))
        choose_adjectives = ''.join(random.choices(adjectives))
        joke = f'{choose_nouns}  {choose_adverbs}  {choose_adjectives}'
        #joke = ' '.join(choose_nouns, choose_adverbs, choose_adjectives)
        jokes.append(joke)
        jokes_quantity -= 1
    return  jokes


if __name__ == "__main__":
    print(get_jokes(3))