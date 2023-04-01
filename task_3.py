def print_file(file, lines):
    print(file.name)
    print(len(lines))
    number = file.name.replace(".txt", "")
    count = 1
    for _ in lines:
        print(f'Строка номер {count} файла номер {number}')
        count += 1
    count = 1


len_file = []
count = 0

with open('1.txt', 'rt', encoding='utf8') as file_1:
    lines_1 = file_1.readlines()
    len_file.append(len(lines_1))
with open('2.txt', 'rt', encoding='utf8') as file_2:
    lines_2 = file_2.readlines()
    len_file.append(len(lines_2))
with open('3.txt', 'rt', encoding='utf8') as file_3:
    lines_3 = file_3.readlines()
    len_file.append(len(lines_3))

while count <= 2:
    if len(lines_1) == min(len_file):
        print_file(file_1, lines_1)
    if len(lines_2) == min(len_file):
        print_file(file_2, lines_2)
    if len(lines_3) == min(len_file):
        print_file(file_3, lines_3)
    len_file.remove(min(len_file))
    count += 1