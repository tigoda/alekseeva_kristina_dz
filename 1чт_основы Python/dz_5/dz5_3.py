from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

students = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
for _ in range(len(tutors)):
    print(next(students))

print(type(students))
