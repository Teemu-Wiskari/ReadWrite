sum_line = []

with open('1.txt', 'r', encoding='utf-8') as file_1:
    sum_line_1 = {}
    score_1 = 0
    for line in file_1.readlines():
        score_1 += 1
        sum_line_1['file_1'] = score_1
        print(sum_line_1)

with open('2.txt', 'r', encoding='utf-8') as file_2:
    sum_line_2 = {}
    score_2 = 0
    for line in file_2.readlines():
        score_2 += 1
        sum_line_2['file_2'] = score_2
        print(sum_line_2)

with open('3.txt', 'r', encoding='utf-8') as file_3:
    sum_line_3 = {}
    score_3 = 0
    for line in file_3.readlines():
        score_3 += 1
        sum_line_3['file_3'] = score_3
        print(sum_line_3)

uniq = dict(list(sum_line_1.items()) + list(sum_line_2.items()) + list(sum_line_3.items()))
print(uniq)
uniq_sorted = sorted(uniq.items(), key=lambda x: x[1])
print(uniq_sorted)
new_dict_unic_sorted = dict(uniq_sorted)
print(new_dict_unic_sorted)
