with open('file1.txt') as f:
    line = 0
    for i in f:
        line += 1
        flag = 0
        word = 0
        for j in i:
            if j != ' ' and flag == 0:
                word += 1
                flag = 1
            elif j == ' ':
                flag = 0

        print(i, len(i) - 1, 'симв.', word, 'сл.')

print(line - 1, 'стр.')
