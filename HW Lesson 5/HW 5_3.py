from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'fff']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
list_of_tuples = ((a, b) for a, b in zip_longest(tutors, klasses))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))
print(next(list_of_tuples))