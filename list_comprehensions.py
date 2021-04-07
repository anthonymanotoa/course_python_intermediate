# lista de los primeros 100 numeros naturales al cuadrado mientas no sean divisibles para 3

def run():
    # natural_numbers = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         natural_numbers.append(i**2)
    # return natural_numbers

    # natural_numbers = [i**2 for i in range(1, 101) if i % 3 != 0]
    # return natural_numbers
    
    # RETO: lista de 1 hasta max 5 digitos que sean multiplos de 4, 6 y 9.
    reto = [i for i in range(1, 100_000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    return reto


if __name__ == '__main__':
    print(run())