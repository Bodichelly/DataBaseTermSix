from random import choice, randint


def get_tags():
    return [
        'ideology',
        'forecast',
        'animals',
        'relations',
        'sports',
        'education',
        'fun',
        'opera'
    ]


def get_random_tags():
    tags_count = randint(0, len(get_tags()) // 2)
    return '' if tags_count == 0 else ','.join(set(choice(get_tags()) for _ in range(tags_count)))
