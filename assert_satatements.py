def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input('Ingresa un número: ')
    # assert int(num) <= 0, 'Debe ser un numero positivo'
    # isnumerio() es un metodo de las str que devuelve True si es 'numero' y False si no
    assert num.isnumeric(), 'Debes ingresar un número'

    print(divisors(int(num)))
    print('Termino mi programa')
    

if __name__ == '__main__':
    run()