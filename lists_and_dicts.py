def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {'fistname': 'Tony', 'lastname': 'Manotoa'}

    super_list = [
        {'fistname': 'Tony', 'lastname': 'Manotoa'},
        {'fistname': 'Angie', 'lastname': 'Paladines'},
        {'fistname': 'Max', 'lastname': 'Medina'},
        {'fistname': 'Jandry', 'lastname': 'Camacho'},
        {'fistname': 'David', 'lastname': 'Pardo'}
    ]

    super_dic = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_num': [-1, -2, 0, 1, 2],
        'float_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dic.items(): # con .items() imprimes tanto el value como la key
        print(key, '-', value)

    print('\n' + '*' * 50 + '\n')

    for dicts in super_list:
        for key, value in dicts.items():
            print(f'{key} - {value}')
        print('-' * 50)
    
    print(my_list, my_dic)

if __name__ == '__main__':
    run()