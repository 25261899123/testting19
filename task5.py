"""
1) Написать скрипт, который проходится по списку и распаковывает ее и если
вдруг внутри списка окажется один индекс под любым типом данных у вас
должна быть ошибка, так как ваш алгоритм всегда проверяет на список, после
вы должны словить ошибку обработать ее в try except, и ваш код должен
продолжать работать, для того чтобы было легче, массив максимум может быть
трех уровневый
Пример:
list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9],
[10, 11, 12]]
в этом массиве допустим ваш алгоритм начинает распаковывать по итерации и
встречает на входе словарь({}) и выдает ошибку Error dict not list, и вы ловите ошибку
обрабатываете и ваш код продолжает работать.
Результат:
# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Соурс код:
list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9], [10,
11, 12]]
new_list = []
for i, x in enumerate(list_):
if type(x) == type([]):
for k in list_[i]:
if type(x) == type([]):
for j in list_[i]:
try:
if type(j) != type([]):
raise Exception("Error")
except Exception:
if j not in new_list and type(j) == type(2):
new_list.append(j)

print(new_list)
Данный код решает проблему попробуйте запустите - ваша задача написать более
эффективный код обязательно должно быть Try Except
"""

def unpuck():
    try:
        list1 = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9],
        [10, 11, 12]]
        list2 = [int(num) for row in list1 for num in row]

    except Exception:
        list2 = [int(num) for row in list1 for num in row if type(num) == (int)]
    finally:
        print(list2)
unpuck()