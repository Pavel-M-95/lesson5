with open('file1.txt', 'w') as f:
    while True:
        for el in input("Введите слово, для выхода нажмите Enter: ").split(' '):
            f.writelines(el + '\n')
        if el == '':
            break
print('Файл записан!')

