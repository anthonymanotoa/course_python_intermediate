def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for i in f:
            numbers.append(int(i))
    print(numbers)


def write():
    names = ['Tony', 'Julio', 'Pepe', 'Christian', 'Rocío']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()