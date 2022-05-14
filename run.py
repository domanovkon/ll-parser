from Parser import Parser

if __name__ == "__main__":
    input_string = '{x = -1 > (p and (1**(-p) = abs(-1))) ;x=p**p ;;x=p}'
    # input_string = '{x = -1 mul p / 1 rem p; ; ; x = p + 1 ** 1 + not p }{;}'
    input_string = input_string.replace(' ', '')
    print('Входная цепочка: ' + input_string + '\n')
    parser = Parser(input_string)