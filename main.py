def print_hi(name):
    print(f'Hi, {name}')
    print('Изменения в файле')
    #  0e41bae80473b133b2591f6d12c563f7295781c2
    print('еще что то меняю')
    #  228d3474a5eed97b11fb69325540652589b87acb


def calc(a, b):
    return a + b


def super_calc(a, c, b):
    return eval(a, c, b)


if __name__ == '__main__':
    print_hi('PyCharm')
    print(calc(10, 15))
    print(super_calc(10, '/', 15))
