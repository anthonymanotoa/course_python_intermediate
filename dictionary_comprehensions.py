# Dictionary with the first 100 natural numbers as its key and numbers**3 as its values
import math

def run():
    # dictionay_naturals = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # return dictionay_naturals

    # CHALLENGE 1000 first natural numbers as keys and sqrt(numbers) as values
    my_dic = {i: math.sqrt(i) for i in range (1, 1001)}
    return my_dic


if __name__ == '__main__':
    print(run())