def thesaurus(*args):
    a = dict()
    for name in args:
        if a.get(name[0]) is None:
            a[name[0]] = [name]
        else:
            a.get(name[0]).append(name)
    return a


print(thesaurus('Иван', 'Марина', 'Игорь', 'Анна', 'Мария', 'Алла'))
