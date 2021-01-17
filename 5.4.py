translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
with open("numbers.txt", 'r') as file_obj:
    try:
        for line in file_obj:
            tokens = line.split(" - ")
            print(tokens)
            if tokens[0] in translater:
                word = translater[tokens[0]]
                result.append(word + ' - ' + tokens[1])
        print(result)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

with open("numbers_new.txt", "w") as file_input:
    try:
        file_input.writelines(result)
    except IOError:
        print("Произошла ошибка ввода-вывода!")
